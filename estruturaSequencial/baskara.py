import math
def baskara():
  print ("estou executando baskara")
  a = input ("valor de a ")
  b = input ("valor de b ")
  c = input ("valor de c ")
  d = b*b - 4*a*c
  print("valor de d", d)
  x1 = (-b + math.sqrt(d))/(2*a)
  print (x1)
  x2 = (-b - math.sqrt(d))/(2*a)
  print(x2)