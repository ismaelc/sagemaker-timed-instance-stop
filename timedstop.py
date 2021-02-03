# Run me to set timer to close your notebook
import threading as th
import boto3

#instance = 'chrisi-idletest'
#seconds = 5.0

def stopInstance(instance):
    print("Stop instance")
    sm = boto3.client('sagemaker')
    sm.stop_notebook_instance(NotebookInstanceName=instance)

def startCountdown(instance, seconds):
    t = th.Timer(seconds, stopInstance(instance))
    t.start() 
