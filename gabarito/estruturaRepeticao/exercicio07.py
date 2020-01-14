# Faça um programa que leia 5 números e informe o maior número.




def substituirReferencia(num1,referenciaMaior):
    if num1 > referenciaMaior:
        referenciaMaior = num1
    return referenciaMaior


def main():

    referenciaMaior = 0

    numList=[]

    for x in range(1,6):
        numInput = float(input("informe o %d número: " % x))
        numList.append(numInput)

    for x in numList:
        referenciaMaior = substituirReferencia(x, referenciaMaior)

    print(referenciaMaior)




# o main só será chamado quando exercutar esse arquivo
if __name__ == "__main__":
   main()
