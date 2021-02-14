from subprocess import call

def shutdown():
    call("sudo shutdown -h now", shell=True)