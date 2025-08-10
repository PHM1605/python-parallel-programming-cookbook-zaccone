import threading, time, random 

# ensure producer() Thread is called BEFORE consumer() Thread
semaphore = threading.Semaphore(0)


def producer():
  global item
  time.sleep(10)
  # create a random item 
  item = random.randint(0, 1000)
  print(f"producer notify: produced item number {item}")
  # this increases semaphore to 1
  semaphore.release()

def consumer():
  print("consumer is waiting.")
  # lock => semaphore->0 when producer already runs; otherwise semaphore=-1->suspending
  semaphore.acquire()
  print(f"consumer notify: consumed item number {item}")


if __name__ == "__main__":
  for i in range(0, 5):
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
  print("program terminated")
