#print de cada elemento dentro do array
def exemplo1():
  fruits = ["banana", "ameixa", "laranja"]
  for fruit in fruits:
    print(fruit)

#print de cada letra da variável tipo string
def exemplo2():
  fruit = "banana"
  for x in fruit:
    print(x)

#print de tudo anterior à banana, incluindo ela
def exemplo3():
  fruits = ["ameixa", "banana", "coco"]
  for fruit in fruits:
    print(fruit)
    if fruit == "banana":
      break

#print de tudo anterior à banana, antes de chegar em banana
def exemplo4():
  fruits = ["ameixa", "banana", "coco"]
  for x in fruits:
    if x == "banana":
      break
    print(x)

#print de todas as combinacoes dos dois arrays
def exemplo5():
  camisetas = ["vermelha", "azul", "branca"]
  calcas = ["jeans", "branca"]

  for x in camisetas:
    for y in calcas:
      print(x, y)

#print de tudo, exceto banana
def exemplo6():
  fruits = ["coco", "banana", "cereja"]
  for x in fruits:
    if x == "banana":
      continue
    print(x)

#print de toda a sequencia de 0 até 5
def exemplo7():
  for x in range(6):
    print(x)