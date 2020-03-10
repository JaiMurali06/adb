import subprocess

def devices():
    return subprocess.check_output('adb devices', shell=True)

def root():
    return subprocess.check_output('adb root', shell=True)

def devicesroot(DSN):
    return subprocess.check_output('adb -s {} root'.format(DSN), shell=True)
