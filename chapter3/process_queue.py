import time, random, multiprocessing 

# <producer> class is responsible for entering 10 items in <queue>
class producer(multiprocessing.Process):
  def __init__(self, queue):
    multiprocessing.Process.__init__(self)
    self.queue = queue 
  
  def run(self):
    for i in range(10):
      item = random.randint(0, 256)
      self.queue.put(item) # pushing to <queue> here
      print(f"Process Producer: item {item} appended to queue {self.name}")
      time.sleep(1)
      print(f"The size of queue is {self.queue.qsize()}")

# <consumer> class pops <item> out of <queue>; ensures it's not empty
class consumer(multiprocessing.Process):
  def __init__(self, queue):
    multiprocessing.Process.__init__(self)
    self.queue = queue 
  
  def run(self):
    while True:
      if self.queue.empty():
        print("the queue is empty")
        break 
      else:
        time.sleep(2)
        item = self.queue.get()
        print(f"Process Consumer: item {item} popped from by {self.name}")
        time.sleep(1)
        

if __name__ == "__main__":
  queue = multiprocessing.Queue()
  process_producer = producer(queue)
  process_consumer = consumer(queue)
  process_producer.start()
  process_consumer.start()
  process_producer.join()
  process_consumer.join()