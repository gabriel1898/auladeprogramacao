

def exercicio2():
	usuario =input("usuario")
	password = input("password")
	while usuario == password:
		print ("error")
		usuario =input("usuario")
		password = input("password")


def main():
	exercicio2()



if __name__ == "__main__":
	main()
