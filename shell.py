import subprocess

def shell(cmd):
    return subprocess.check_output('adb shell {}'.format(cmd), shell=True)

def devicesshell(DSN, cmd):
    return subprocess.check_output('adb -s {} shell {}'.format(DSN, cmd), shell=True)
