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


usage = """
  arg usage: <function> <function args>
  functions: primes <num>
             lcm    <a> <b>
             hcf    <a> <b>
             r_primes <range_max>
             r_lcm    <range_max>
             r_hcf    <range_max>
             r_hcf    <range_max_a> <range_max_b>
             r_hcf    <range_max_a> <range_max_b> <res_min>
"""


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
  print(f"hcf({a}, {b}) = {res}")
  print_primes(a)
  print_primes(b)
  print_primes(res)
  print("")

def r_primes(range_max):
  if range_max <= 2:
    # TODO: print error
    return
  
  for i in range(2, range_max):
    print_primes(i)

def r_lcm(range_max):
  if range_max <= 2:
    # TODO: print error
    return

  for i in range(2, range_max):
    for j in range((i+1), range_max):
      print_lcm(i, j)

def r_hcf(range_max_a, range_max_b, res_min):
  if range_max_a <= 2 or (range_max_b and range_max_b <2):
    # TODO: print error
    return

  if not range_max_b:
    range_max_b = range_max_a
  
  for i in range(2, range_max_a):
    for j in range((i+1), range_max_b):
      if res_min and hcf(i, j) < res_min:
        continue
      
      print_hcf(i, j)

def func(funcArg, a, b=None, c=None):
  match funcArg:
    case("usage"):
      print(usage)
    case("primes"):
      print_primes(a)
    case("lcm"):
      print_lcm(a, b)
    case("hcf"):
      print_hcf(a, b)
    case("r_primes"):
      r_primes(a)
    case("r_lcm"):
      r_lcm(a)
    case("r_hcf"):
      r_hcf(a, b, c)

if len(argv) >= 2:
  funcArg = argv[1]

  if len(argv) >= 3:
    a = int(argv[2])
  else:
    a = None

  if len(argv) >= 4:
    b = int(argv[3])
  else:
    b = None

  if len(argv) >= 5:
    c = int(argv[4])
  else:
    c = None
    
  func(funcArg, a, b, c)

  
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
