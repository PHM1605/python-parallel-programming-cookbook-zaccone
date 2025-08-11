from threading import Thread 
from queue import Queue 
import time, random 

class Producer(Thread):
  def __init__(self, queue):
    Thread.__init__(self)
    self.queue = queue 
  
  def run(self):
    # produce 5 items
    for i in range(5):
      item = random.randint(0, 256)
      self.queue.put(item) # acquire Lock & put Item to Queue
      print(f"Producer notify: item {item} appended to queue by {self.name}")
      time.sleep(1)

class Consumer(Thread):
  def __init__(self, queue):
    Thread.__init__(self)
    self.queue = queue 
  
  def run(self):
    while True:
      item = self.queue.get() # acquire Lock & remove data from Queue 
      print(f"Consumer notify: {item} popped from queue by {self.name}")
      self.queue.task_done()

if __name__ == "__main__":
  queue = Queue()
  t1 = Producer(queue)
  t2 = Consumer(queue)
  t3 = Consumer(queue)
  t4 = Consumer(queue)

  t1.start()
  t2.start()
  t3.start()
  t4.start()

  t1.join()
  t2.join()
  t3.join()
  t4.join()
