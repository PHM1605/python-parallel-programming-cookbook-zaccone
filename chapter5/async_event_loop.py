# task A calls B, task B calls C, task C calls A....
# time of execution of each task is random
import asyncio, time, random 

def task_A(end_time, loop):
  print("task_A called")
  time.sleep(random.randint(0, 5))
  if loop.time()+1.0 < end_time:
    loop.call_later(1, task_B, end_time, loop) # start task_B(end_time, loop) after 1 seconds
  else:
    loop.stop()

def task_B(end_time, loop):
  print("task_B called")
  time.sleep(random.randint(4,7))
  if loop.time()+1.0 < end_time:
    loop.call_later(1, task_C, end_time, loop) # start task_C(end_time, loop) after 1 seconds
  else:
    loop.stop()

def task_C(end_time, loop):
  print("task_C called")
  time.sleep(random.randint(5,10))
  if loop.time()+1.0 < end_time:
    loop.call_later(1, task_A, end_time, loop) # start task_A(end_time, loop) after 1 seconds
  else:
    loop.stop()

loop = asyncio.get_event_loop()
end_loop = loop.time() + 60 # total process has 60s duration
loop.call_soon(task_A, end_loop, loop) # this function will be called as soon as mainloop starts
loop.run_forever() # mainloop, runs until loop.stop() some where in callback function
loop.close()
