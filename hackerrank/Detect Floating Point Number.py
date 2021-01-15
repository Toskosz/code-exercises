import re
t = int(input())
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
for _ in range(0,t):
    n = input()
    if not isfloat(n):
        print("False")
    elif (re.match('\+-', n)) or (re.match('-\+', n)):
        print("False")
    elif not re.search("\.\d", n):
        print("False")
    elif not re.search("\.", n):
        print("False")
    else:
        print("True")