# thread 0->4 will print in undetermined order
import threading, time, random

def function(i):
  time.sleep(random.random() * 0.05) # simulate different thread running time
  print(f"function called by thread {i}\n")
  return 

threads = []
for i in range(5):
  t = threading.Thread(target=function, args=(i,))
  threads.append(t)
  t.start()

# Note: this will wait until EACH of the thread has finished his/her task before exiting the Python PROCESS
for i in threads:
  t.join()
