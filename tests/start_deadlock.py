import pthreading
pthreading.monkey_patch()

import signal
import threading
import time

import yappi

def run():
    pass

signal.alarm(1)
thread = threading.Thread(target=run)
thread.daemon = True
thread.start()
yappi.start()
thread.join()
yappi.stop()
