from threading import Thread 
from time import sleep 

class CookBook(Thread):
  def __init__(self):
    Thread.__init__(self)
    self.message = "Hello Parallel Python Cookbook!!\n"
  
  def print_message(self):
    print(self.message)
  
  # this function will be called after start()
  def run(self):
    print("Thread Starting\n")
    x = 0
    while (x<10):
      self.print_message()
      sleep(2)
      x += 1
    print("Thread Ended\n")
  
print("Process Started")
hello_Python = CookBook()
hello_Python.start() # after starting, it will run() Thread in background
print("Process Ended") # this will print first 

