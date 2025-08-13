import multiprocessing

# process 0 prints nothing; process 1 prints 0; ...
def myFunc(i):
  print(f"calling myFunc from process number: {i}")
  for j in range(0,i):
    print(f'output from myFunc is: {j}')

if __name__ == "__main__":
  for i in range(6):
    process = multiprocessing.Process(target=myFunc, args=(i,))
    process.start()
    process.join()
