from IPython.display import clear_output, display
from datetime import datetime, timezone
import threading
import boto3
import re
import os
from tqdm import tqdm

sm = boto3.client('sagemaker')

def setInterval(interval):
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop(): # executed in another thread
                while not stopped.wait(interval): # until stopped
                    function(*args, **kwargs)

            t = threading.Thread(target=loop)
            t.daemon = True # stop if the program exits
            t.start()
            return stopped
        return wrapper
    return decorator



@setInterval(1)
def idlestop(instanceName, time):    
    instance = findInstance(instanceName)
    if instance:
        clear_output(wait=True)
        print(f'Found {instance["NotebookInstanceName"]}')
    else: 
        print(f'No `{instanceName}` instance found. Run `stop.set()` in another cell to stop timer.')
        return
    
    if instance and hitIdleLimit(instance, time):
        print('Instance stop!')
        stopInstance(instance["NotebookInstanceName"])
        
def findInstance(instanceName):
    i = {}
    instances = sm.list_notebook_instances()
    for instance in instances['NotebookInstances']:
        if instance['NotebookInstanceStatus'] == 'InService' \
        and instance['NotebookInstanceName'].count(instanceName) > 0:
            i = instance
            break
    return i

def stopInstance(instance):
    sm.stop_notebook_instance(NotebookInstanceName=instance)

def hitIdleLimit(instance, idleLimit=18000): #5 hours
    idle_secs = getIdleSecs(instance)
    idleLimit = resolveTime(idleLimit)
    displayProgress(idle_secs, idleLimit)
    return  idle_secs > idleLimit

def getIdleSecs(instance):
    #now = datetime.now(timezone.utc)
    now = datetime.now()
    tmp = os.popen("ls -lt --time-style=full-iso").readlines()[1].split()
    str_date = f'{tmp[5]} {tmp[6]}'[:-3]
    lastUsed = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=None)
    
    #lastUsed = instance['LastModifiedTime'] #.replace(tzinfo=None)    
    idle_secs = (now - lastUsed).total_seconds()
    #clear_output(wait=True)
    print(f'Now:  {now}\nLast: {lastUsed}\nIdle: {idle_secs}')
    
    return idle_secs
    
def resolveTime(time):
    if isinstance(time, int) or isinstance(time, float):
        return time
    elif isinstance(time, str):
        texts = time.lower().split()
        items = []
        for t in texts:
            match = re.match(r"([0-9]+)([a-z]+)", t)
            if match:
                items.append(match.groups())

        time = 0
        for i in items:
            hourCheck = any(item in list(i)
                            for item in ['h', 'hr', 'hour', 'hours'])
            minCheck = any(item in list(i)
                           for item in ['m', 'min', 'mins', 'minute', 'minutes'])
            secCheck = any(item in list(i)
                           for item in ['s', 'sec', 'secs', 'second', 'seconds'])

            if hourCheck:
                time += int(list(i)[0]) * 3600
            if minCheck:
                time += int(list(i)[0]) * 60
            if secCheck:
                time += int(list(i)[0])

        return time
    

def displayProgress(current, maximum):
    progress = int((100*current)/maximum)
    for i in range(100):
        if i < progress: print('=', end="")
        elif i == progress: print('>', end="")
        else: print('.', end="")
    print(f' ({progress}%)')
    #return progress 