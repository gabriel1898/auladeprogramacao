def imprimirLoop(vezes):
	i = 0
	while i <= vezes:
		print (i)
		i += 1

def banana(vezes, onOff):
	if onOff == True:
		i = 0
		while i <= vezes:
			print (i)
			if i == (vezes - 2):
				break
			i += 1
	if onOff == False:
		imprimirLoop(vezes)

def main():

	vezes = int(input("quantas vezes deseja imprimir?"))
	onOff = input ("is onOff true or false?   T for True   or   F for False")
	while onOff != "T" and onOff != "F": 
		onOff = input ("is onOff true or false?   T for True   or   F for False")
	if onOff =="T":
		onOff = True
	if onOff =="F":
		onOff = False
	banana(vezes, onOff)
	print(type(onOff))

#	vezes = int(input("quantas vezes deseja imprimir? "))
#	imprimirLoop(vezes)

if __name__ == "__main__":
	main()