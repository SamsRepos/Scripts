
# https://people.revoledu.com/kardi/tutorial/BasicMath/Prime/Algorithm-PrimeFactor.html

def prime_factors(n):
  res = list()
  p = 2
  while n >= (p**2):
    if (n % p) == 0:
      res.append(int(p))
      n /= p
    else:
      p += 1
  res.append(int(n))

  if len(res) == 0:
    return [int(n)]
  else:
    return res

def hcf(a, b):
  a_primes = prime_factors(a)
  b_primes = prime_factors(b)

  hcf_primes = list()
  for x in a_primes:
    if x in b_primes:
      b_primes.remove(x)
      hcf_primes.append(x)  

  res = 1
  for x in hcf_primes:
    res *= x
  return res

def lcm(a, b):
  a_primes = prime_factors(a)
  b_primes = prime_factors(b)

  lcm_primes = list()
  for x in a_primes:
    lcm_primes.append(x)
    if x in b_primes:
      b_primes.remove(x)

  for x in b_primes:
    lcm_primes.append(x)

  res = 1
  for x in lcm_primes:
    res *= x
  return res



RANGE = 25

"""
for i in range(2, RANGE):
  print(repr(i) + ":")
  print(" " + repr(prime_factors(i)))
  print("")    
"""

"""
for i in range(2, RANGE):
  for j in range((i+1), RANGE):
    res = lcm(i, j)
    print(f"lcm({i}, {j}) = {res}")
"""

"""
for i in range(2, RANGE):
  for j in range((i+1), RANGE):x
    res = hcf(i, j)
    if res > 1:
      print(f"hcf({i}, {j}) = {res}")
"""

for i in range(2, RANGE):
  for j in range((i+1), RANGE):
    res = lcm(i, j)
    if res == i * j or res == i or res == j:
      continue
    print(f"lcm({i}, {j}) = {res}")
    print(f"{i}: {prime_factors(i)}")
    print(f"{j}: {prime_factors(j)}")
    print(f"{res}: {prime_factors(res)}")
    print("")
