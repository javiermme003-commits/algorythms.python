
def esprimo(n):
  is_prime = True
  m = 1
  while n - m > 1:
      if n % (n-m) == 0:
        is_prime = False
        break
      
      m = m + 1
  if n<2:
    is_prime = False

  return is_prime
