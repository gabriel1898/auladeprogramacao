def validarNome():
	name = input(" user name ")
	i = 0
	for x in name:
		i += 1
	while i <=3:
		print ("error")
		name = input(" user name ")
		i = 0
		for x in name:
			i += 1
	else:
			print ("valid")

def idade():
	idade = int(input(" idade "))
	while idade > 150 or idade < 0:
		print ("error")
		idade = int(input(" idade "))
	else:
		print ("valid")

def salario():
	salario = int(input(" salario "))
	while salario < 0:
		print ("error")
		salario = int(input(" salario "))
	else:
		print ("valid")

def sexo():
	pessoa = input(" sexo:  (f for feminino)  or  (m for masculino) ")
	while pessoa != "f" and pessoa != "m":
		print ("invalid")
		pessoa = input(" sexo:  (f for feminino)  or  (m for masculino) ")
	else:
		print ("valid")

def estadoCivil():
	pessoa = input(" estado civil:  (s for solteiro)  or  (c for casado)  or  (v for viuvo)  or  (d for divorciado)")
	while pessoa != "s" and pessoa != "c" and pessoa !="v" and pessoa !="d":
		print ("invalid")
		pessoa = input(" estado civil:  (s for solteiro)  or  (c for casado)  or  (v for viuvo)  or  (d for divorciado)")
	else:
		print ("valid")


def main():
	validarNome()
	idade()
	salario()
	sexo()
	estadoCivil()


if __name__ == "__main__":
	main()