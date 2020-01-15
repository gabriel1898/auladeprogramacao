#def seIgual(usuario, password):
#	if usuario == password:
#		return True
#	else:
#		return False

def exercicio2():
	usuario =input("usuario")
	password = input("password")
	while usuario == password:
		print ("error")
		usuario =input("usuario")
		password = input("password")

#	for x in usuario:
#		print("x", x)
#		for y in password:
#			print("y", y)
#			if x == y:
#				print ("error", x)

def main():
	exercicio2()

#	usuario =input("usuario")
#	password = input("password")
#	while seIgual(usuario, password):
#		print ("error")
#		usuario =input("usuario")
#		password = input("password")


if __name__ == "__main__":
	main()
