# Faça um programa que leia 5 números e informe a soma e a média dos números.


def pedirNumeros(quantNum):
    numeros = []
    for x in range(quantNum):
        num = float(input("digite um numero: "))
        numeros.append(num)
    return numeros

def somarNumeros(numeros):
    soma = 0
    for x in numeros:
        soma += x
    return soma


def main():
    quantNum = 5
    numeros = pedirNumeros(quantNum)
    soma = somarNumeros(numeros)
    media = soma/quantNum
    print("soma: ", soma)
    print("media: ", media)



if __name__ == "__main__":
   main()
