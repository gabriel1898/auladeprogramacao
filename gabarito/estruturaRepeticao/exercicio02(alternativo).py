def seIgual(usuario, password):
  if usuario == password:
      return True
  else:
      return False


  for x in usuario:
      print("x", x)
      for y in password:
          print("y", y)
          if x == y:
              print ("error", x)


  usuario =input("usuario")
  password = input("password")
  while seIgual(usuario, password):
      print ("error")
      usuario =input("usuario")
      password = input("password")
