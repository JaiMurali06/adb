import subprocess

def install(cmd):
    return subprocess.check_output('adb install {}'.format(cmd), shell=True)

def devicesinstall(DSN, cmd):
    return subprocess.check_output('adb -s {} install {}'.format(DSN, cmd), shell=True)

def replcae(cmd):
    return subprocess.check_output('adb install -r {}'.format(cmd), shell=True)

def devicesreplace(DSN, cmd):
    return subprocess.check_output('adb -s {} install -r {}'.format(DSN, cmd), shell=True)

