# Run me to set timer to close your Sagemaker instance
import threading as th
import boto3

def setCountdown(instance, seconds):
    return th.Timer(float(seconds), stopInstance, [instance])

def stopInstance(instance):
    print("Stop instance")
    sm = boto3.client('sagemaker')
    sm.stop_notebook_instance(NotebookInstanceName=instance)

