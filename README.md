# sagemaker-timed-instance-stop

### To use
In your Sagemaker Jupyter notebook (Python), copy the snippets below to your notebook cells in order:

Description | Code
------ | ------
Download script into your instance   | `!wget -O timedstop.py https://raw.githubusercontent.com/ismaelc/sagemaker-timed-instance-stop/main/timedstop.py`
Import library | `from timedstop import setCountdown`
Initialize timer | `t = setCountdown('<instance name>', <seconds>)`
Start timer | `t.start()`
Stop timer | `t.cancel()`
