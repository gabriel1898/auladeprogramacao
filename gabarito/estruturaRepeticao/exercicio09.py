# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def calcularImpares(numMin, numMax):
    numImpares = []
    if numMin%2 != 0:
        for x in range(numMin, numMax, 2):
            numImpares.append(x)
    else:
        numMin = numMin - 1
        for x in range(numMin, numMax, 2):
            numImpares.append(x)
    return numImpares

def main():
    numImpares = calcularImpares(1, 50)
    print(numImpares)


if __name__ == "__main__":
   main()
