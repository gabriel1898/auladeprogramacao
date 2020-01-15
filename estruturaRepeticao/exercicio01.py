def exercicio1():
	p = float(input("qual é a nota?"))
	while p >= 10 or p <= 0:
		print ("invalid")
		p = float(input("qual é a nota?"))
	print ("valor correto")


def main():
	exercicio1()


if __name__ == "__main__":
	main()



