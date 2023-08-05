from sys import argv

# prime factors algorithm:
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


# arg usage: <function> <function args>
# functions: primes <num>
#            lcm    <a> <b>
#            hcf    <a> <b>
#            rprimes <rangemax>
#            rlcm    <rangemax>
#            rhcf    <rangemax>

def print_primes(a):
  print(f"{a}: {prime_factors(a)}")

def print_lcm(a, b):
  res = lcm(a, b)
  print(f"lcm({a}, {b}) = {res}")
  print_primes(a)
  print_primes(b)
  print_primes(res)
  print("")
  
def print_hcf(a, b):
  res = hcf(a, b)
  print(f"lcm({a}, {b}) = {res}")
  print_primes(a)
  print_primes(b)
  print_primes(res)
  print("")

def rprimes(range_max):
  if range_max <= 2:
    # TODO: print error
    return
  
  for i in range(2, range_max):
    print_primes(i)

def rlcm(range_max):
  if range_max <= 2:
    # TODO: print error
    return

  for i in range(2, range_max):
    for j in range((i+1), range_max):
      print_lcm(i, j)

def rhcf(range_max):
  if range_max <= 2:
    # TODO: print error
    return

  for i in range(2, range_max):
    for j in range((i+1), range_max):
      print_hcf(i, j)

def func(funcArg, a, b=None):
  match funcArg:
    case("primes"):
      print_primes(a)
    case("lcm"):
      print_lcm(a, b)
    case("hcf"):
      print_hcf(a, b)
    case("rprimes"):
      rprimes(a)
    case("rlcm"):
      rlcm(a)
    case("rhcf"):
      rhcf(a)

if len(argv) > 2:
  funcArg = argv[1]
  a = int(argv[2])
  if len(argv) == 3:
    func(funcArg, a)
  elif len(argv) == 4:
    b = int(argv[3])
    func(funcArg, a, b)


  
"""  
RANGE = 25

for i in range(2, RANGE):
  print(repr(i) + ":")
  print(" " + repr(prime_factors(i)))
  print("")    

for i in range(2, RANGE):
  for j in range((i+1), RANGE):
    res = lcm(i, j)
    print(f"lcm({i}, {j}) = {res}")

for i in range(2, RANGE):
  for j in range((i+1), RANGE):x
    res = hcf(i, j)
    if res > 1:
      print(f"hcf({i}, {j}) = {res}")

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
"""
