# sagemaker-timed/idle-instance-stop

### Idle Stop
![](https://i.postimg.cc/VsHzRXcZ/idlestop.gif)

In your Sagemaker Jupyter notebook (Python), copy the snippets below to your notebook cells in order:

Description | Code
------ | ------
Download script into your instance   | `!aws s3 cp s3://labs-us-ml-scripts/chrisi/workspace/scripts/idlestop/idlestop.py .`
Import library  | `from idlestop import idlestop`
Run timer | `stop = idlestop('<instance name>, '<time>')` time can be of format "1h 25min", "5hours", "25mins 6s", etc.`
(Optional) Cancel timer | `stop.set()`
--
### Timed Stop
![](https://i.postimg.cc/Kz1zkGdq/sagemakertimedstop.png)
In your Sagemaker Jupyter notebook (Python), copy the snippets below to your notebook cells in order:

Description | Code
------ | ------
Download script into your instance   | `!aws s3 cp s3://labs-us-ml-scripts/chrisi/workspace/scripts/idlestop/timedstop.py .`
Import library | `from timedstop import setCountdown`
Initialize timer | `t = setCountdown('<instance name>', <time>)` or `setCountdown(...).start()` if you don't need cancel manually 
 _ | e.g. ` t = setCountdown('chrisi-timedtest-5cht', 3600)`. **time** if sent without quotes is in _seconds_. If sent with quotes, they can take the following format examples - "1hr 30min", "1hour 20s", "8hours", "45mins", and so on. Make sure to split the hours, minutes, and seconds.
Start timer | `t.start()`
(Optional) Stop timer | `t.cancel()` --> In case you need to stop the countdown timer
