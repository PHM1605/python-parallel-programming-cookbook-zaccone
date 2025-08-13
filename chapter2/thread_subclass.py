import time, threading 

exitFlag = 0

class myThread(threading.Thread):
  def __init__(self, threadID, name, delay):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name 
    self.delay = delay #
  
  def run(self):
    print("Starting " + self.name)
    print_time(self.name, self.delay, 5)  # always print 5 times 
    print("Exiting " + self.name)

# print <counter> times, each delays <delay> seconds
def print_time(threadName, delay, counter):
  while counter:
    if exitFlag: 
      thread.exit()
    time.sleep(delay)
    print(f"{threadName}: {time.ctime(time.time())}")
    counter -= 1

# main part
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()
thread1.join() # ensure thread-1 compleletely finishes
thread2.join() # this delaying thread still runs till here
print("Exiting Main Thread")