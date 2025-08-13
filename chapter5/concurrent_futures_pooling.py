import concurrent.futures
import time 

number_list = list(range(1,11))

# do something to waste time 
def count(number):
  for i in range(0, 100_000_000):
    i += 1
  return i*number 

def evaluate(item):
  result_item = count(item)
  print(f"Item {item}, result {result_item}")

# for list [1,2,...,10]
if __name__ == "__main__":
  # sequentially
  start_time = time.perf_counter()
  for item in number_list:
    evaluate(item)
  print(f"Sequential Execution in {time.perf_counter()-start_time} seconds")
  # thread pool
  start_time = time.perf_counter()
  with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for item in number_list:
      executor.submit(evaluate, item)
  print(f"Thread Pool Execution in {time.perf_counter() - start_time} seconds")
  # process pool - this will be the fastest
  start_time = time.perf_counter()
  with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    for item in number_list:
      executor.submit(evaluate, item)
  print(f"Process Pool Execution in {time.perf_counter()-start_time} seconds")
  