def exercicio4():
	anos = 0
	A = 80000
	i = 0.03
	B = 200000
	j = 0.015
	while A < B:
		A = A + A*i
		B = B + B*j
		anos +=1
	else:
		print ("conclued")
	print (" a quantidade de anos foi: ", anos)














def main():
	exercicio4()

if __name__ == "__main__":
	main()