import asyncio

async def factorial(number):
  f = 1
  for i in range(2, number+1):
    print(f"Asyncio.Task: Compute factorial ({i})")
    await asyncio.sleep(1)
    f *= i 
  print(f"Asyncio.Task - factorial ({number}) = {f}")

# number = #elements in fibo sequence
async def fibonacci(number):
  a, b = 0, 1
  for i in range(number):
    print(f"Asyncio.Task: Compute fibonacci ({i})")
    await asyncio.sleep(1)
    a, b = b, a+b
  print(f"Asyncio.Task - fibonacci({number}) = {a}")

# bino_coeff = n! / (k! * (n-k)!) 
# notice that n! / (n-k)! with n=20, k=10 => 11*12*..*20
async def binomial_coefficient(n, k):
  result = 1 
  for i in range(1, k+1):
    # denominator = k!
    result = result * (n-i+1)/i 
    print(f"Asyncio.Task: Compute binomial_coefficient ({i})")
    await asyncio.sleep(1)
  print(f"Asyncio.Task - binomial_coefficient({n},{k})={result}")

if __name__ == "__main__":
  task_list = [
    asyncio.Task(factorial(10)),
    asyncio.Task(fibonacci(10)),
    asyncio.Task(binomial_coefficient(20,10))
    ]
  loop = asyncio.get_event_loop()
  loop.run_until_complete(asyncio.wait(task_list))
  loop.close()