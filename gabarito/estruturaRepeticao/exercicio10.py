# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.


def calcularInteiros(numMin, numMax):
    numInteiros = []
    for x in range(numMin + 1, numMax):
        numInteiros.append(x)
    return numInteiros

def main():
    numMin = int(input("qual o menor numero? "))
    numMax = int(input("qual o maior numero? "))
    numInteiros = calcularInteiros(numMin, numMax)
    for x in numInteiros:
        print(x)

if __name__ == "__main__":
   main()

