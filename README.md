# sagemaker-timed-instance-stop

### To use
In your Sagemaker Jupyter notebook (Python), run these commands in separate cells:

 
    !wget -O timedstop.py https://raw.githubusercontent.com/ismaelc/sagemaker-timed-instance-stop/main/timedstop.py
 --
    
    from timedstop import setCountdown
    setCountdown('<instance name>', <seconds>).start()
    #  setCountdown('chrisi-idletest', 3600).start()
