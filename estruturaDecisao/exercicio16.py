import math
def exercicio16():
  a = 1
  b = 2
  c = 1
  d = b*b - 4*a*c
  x1 = (-b + math.sqrt(d))/(2*a)
  x2 = (-b - math.sqrt(d))/(2*a)
  if (a == 0):
    print ("encerrado")
  if (d < 0):
    print ("encerrado")
  if (d == 0):
    print (x1)
  if (d > 0):
    print (x1, x2)