def fibonacci(n):
  if n == 1 or n == 2: return 1
  return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memoization(n):
  fibo = dict()
  def rec(n):
    if n in fibo: return fibo[n]

    if n == 1 or n == 2:
      fibo[n] = 1
    else:
      fibo[n] = rec(n - 1) + rec(n - 2)
    return fibo[n]
  return rec(n)

def fibonacci_bottom_up(n):
  if n == 1 or n == 2: return 1

  fib0 = 1
  fib1 = 1
  for i in range(3, n+1):
    new_fib = fib0 + fib1
    fib0 = fib1
    fib1 = new_fib
  return fib1