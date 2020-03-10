import subprocess, time

def check_if_keywork(key, timeout):
    start_time = time.time()
    proc = subprocess.Popen(['adb', 'logcat', '-v', 'threadtime'], stdout=subprocess.PIPE)
    for line in proc.stdout:
        if key in line:
            proc.kill()
            return 'Succes'
        else:
            pass
        if time.time() - start_time > timeout:
            return 'Failure'
    return 'Failure'