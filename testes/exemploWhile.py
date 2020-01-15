def imprimirLoop(vezes):
	i = 0
	while i <= vezes:
		print (i)
		i += 1

def main():
	vezes = int(input("quantas vezes deseja imprimir? "))
	imprimirLoop(vezes)

if __name__ == "__main__":
	main()