# Run me to set timer to close your Sagemaker instance
import threading as th
import boto3
import regex


def setCountdown(instance, time):
    # return th.Timer(float(seconds), stopInstance, [instance])
    return th.Timer(resolveTime(time), stopInstance, [instance])


def stopInstance(instance):
    print("Stop instance")
    sm = boto3.client('sagemaker')
    sm.stop_notebook_instance(NotebookInstanceName=instance)


def resolveTime(time):
    if isinstance(time, int) or isinstance(time, float):
        return time
    elif isinstance(time, str):
        texts = time.lower().split()
        items = []
        for t in texts:
            match = regex.match(r"([0-9]+)([a-z]+)", t)
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
