from random import random
from math import sqrt


def rand_coord():
    res = random() # 0 <= res <= 1
    # res -= 0.5     # -0.5 <= res <= 0.5
    # res *= 2       # -1 <= res <= 1
    return res
    
def pi_estimate(its):
  prob = 0

  for i in range(its):
    x = rand_coord()
    y = rand_coord()
    hypotenuse = sqrt( (x ** 2) + (y ** 2) )
    if hypotenuse < 1: # 1 is the radius
      prob += 1
    # now probability var is the number of times it landed
  prob /= its # bring it down to a fraction < 1
  pi = prob  * 4 # since the square's area is 4, multiply by 4 for PI
  return pi

for i in range(10):
  its = 10 ** i
  print("throwing " + repr(its) + " darts...")
  pi = pi_estimate(its)
  print("pi estimate: " + repr(pi))
  print("")

