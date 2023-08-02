from math import sqrt

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
  
pows(1000, 2)



