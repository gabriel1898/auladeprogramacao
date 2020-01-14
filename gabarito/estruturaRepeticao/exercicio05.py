#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

from exercicio04 import calcularAnos


 #estrutura condicional para poder inverter os dados, caso a população de A seja maior
def inverterDados(populacaoA, populacaoB, crescimentoA, crescimentoB):
    if populacaoA > populacaoB:
        populacaoA, populacaoB = populacaoB, populacaoA
        crescimentoA, crescimentoB = crescimentoB, crescimentoA

def main():
    refazer = 's'
    while(refazer == 's'):
        populacaoA = int(input("informe a população do país A: "))
        populacaoB = int(input("informe a população do país B: "))
        crescimentoA = float(input("informe a taxa de crescimento país A: "))
        crescimentoB = float(input("informe a taxa de crescimento país B: "))

        inverterDados(populacaoA, populacaoB, crescimentoA, crescimentoB)

        print(calcularAnos(populacaoA, populacaoB, crescimentoA, crescimentoB))

        refazer = input("deseja refazer os calculos? [s ou n] ")


# o main só será chamado quando exercutar esse arquivo
if __name__ == "__main__":
   main()
