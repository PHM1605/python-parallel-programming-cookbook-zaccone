import logging 
import threading 
import time 

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition() 

class Consumer(threading.Thread):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
  
  def consume(self):
    with condition:
      if len(items) == 0:
        loggin.info('no items to consume')
        condition.wait()
      items.pop()
      logging.info('consumed 1 item')
      condition.notify()
  
  def run(self):
    for i in range(20):
      time.sleep(2)
      self.consume()

class Producer(threading.Thread):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
  
  def produce(self):
    with condition:
      if len(items) == 10:
        logging.info('items produced {}. Stopped'.format(len(items)))
        condition.wait()
      items.append(1)
      logging.info('total items {}'.format(len(items)))
      condition.notify()
  
  def run(self):
    for i in range(20):
      time.sleep(0.5)
      self.produce()

if __name__ == "__main__":
  t1 = Producer()
  t2 = Consumer()
  t1.start()
  t2.start()
  t1.join()
  t2.join()
