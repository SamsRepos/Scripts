from math import sqrt
from sys import argv

def pows(its = 10, pow = 2):
  for a in range(1, its):
    for b in range((a+1), its):
      
      c = ( (a**pow) + (b**pow) ) ** (1/pow)

      if((c % 1) != 0):
        continue

      aStr = f"{a}^{pow}"
      bStr = f"{b}^{pow}"
      cStr = f"{c}^{pow}"
            
      print(f"{aStr} + {bStr} = {cStr}")

DEFAULT_ITS = 1000
DEFAULT_POW = 2


if len(argv) == 3:
  try:
    its = int(argv[1])
    pow = int(argv[2])
  except:
    print("Error: args should be int values: <iterations> <power>")
    exit()
else:
  its = DEFAULT_ITS
  pow = DEFAULT_POW
        
pows(its, pow)



