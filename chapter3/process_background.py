# if process in background => prints 0..4
# if process in foreground => print 5..9
import time 
import multiprocessing 

def foo():
  name = multiprocessing.current_process().name 
  print(f"Starting {name} \n")
  if name == "background_process":
    for i in range(0,5):
      print(f"---> {i} \n")
      time.sleep(1)
  else:
    for i in range(5,10):
      print(f"---> {i} \n")
    print(f"Exiting {name}\n")

if __name__ == "__main__":
  background_process = multiprocessing.Process(name="background_process", target=foo)
  background_process.daemon = True 
  NO_background_process = multiprocessing.Process(name="NO_background_process", target=foo)
  NO_background_process.daemon = False 
  background_process.start()
  NO_background_process.start()
  # background_process.join() # won't see daemon effect if see this task
  # NO_background_process.join() 
