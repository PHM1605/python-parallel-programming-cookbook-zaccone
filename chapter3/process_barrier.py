# we'll create 4 process, 2 with barrier and 2 without
import multiprocessing 
from multiprocessing import Barrier, Lock, Process 
from time import time 
from datetime import datetime 

def test_with_barrier(synchronizer, serializer):
  name = multiprocessing.current_process().name 
  synchronizer.wait() # both p1 and p2 wait here before printing
  now = time()
  # ensure <lock> so that 2 processes don't access this at same time
  with serializer:
    print(f"process {name} --> {datetime.fromtimestamp(now)}")

def test_without_barrier():
  name = multiprocessing.current_process().name 
  now = time() 
  print(f"process {name} --> {datetime.fromtimestamp(now)}")

if __name__ == "__main__":
  synchronizer = Barrier(2) # how many <process> should the <barrier> waits
  serializer = Lock()
  # with <barrier>, <p1> and <p2> will print same time
  Process(name="p1 - test_with_barrier", target=test_with_barrier, args=(synchronizer,serializer)).start()
  Process(name="p2 - test_with_barrier", target=test_with_barrier, args=(synchronizer,serializer)).start()
  # normal runs are not synchronized => different time 
  Process(name="p3 - test_without_barrier", target=test_without_barrier).start()
  Process(name="p4 - test_without_barrier", target=test_without_barrier).start()

