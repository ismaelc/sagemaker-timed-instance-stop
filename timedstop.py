# Run me to set timer to close your notebook
import threading as th
import boto3

def stopInstance(instance):
    print("Stop instance")
    sm = boto3.client('sagemaker')
    sm.stop_notebook_instance(NotebookInstanceName=instance)

def setCountdown(instance, seconds):
    return th.Timer(float(seconds), stopInstance, [instance])