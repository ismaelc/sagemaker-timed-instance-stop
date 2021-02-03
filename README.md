# sagemaker-timed-instance-stop

![](https://i.postimg.cc/Kz1zkGdq/sagemakertimedstop.png)

### To use
In your Sagemaker Jupyter notebook (Python), copy the snippets below to your notebook cells in order:

Description | Code
------ | ------
Download script into your instance   | `!wget -O timedstop.py https://raw.githubusercontent.com/ismaelc/sagemaker-timed-instance-stop/main/timedstop.py`
Import library | `from timedstop import setCountdown`
Initialize timer | `t = setCountdown('<instance name>', <time>)` or `setCountdown(...).start()` if you don't need cancel manually 
 _ | e.g. ` t = setCountdown('chrisi-timedtest-5cht', 3600)`. **time** if sent without quotes is in _seconds_. If sent with quotes, they can take the following format examples - "1hr 30min", "1hour 20s", "8hours", "45mins", and so on. Make sure to split the hours, minutes, and seconds.
Start timer | `t.start()`
Stop timer | `t.cancel()`
