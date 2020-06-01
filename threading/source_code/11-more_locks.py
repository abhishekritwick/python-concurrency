import threading

lock = threading.Lock()
lock.acquire()
# lock.acquire() -> deadlock!

rlock = threading.RLock()
rlock.acquire()
rlock.acquire() # no deadlock!
print(rlock)
rlock.release()
print(rlock)
print(threading.current_thread())