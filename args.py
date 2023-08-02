from sys import argv

print(f"Number of arguments: {len(argv)}")
print(f"Arg list: {str(argv)}")

for i in range(len(argv)):
  print(argv[i])
  
