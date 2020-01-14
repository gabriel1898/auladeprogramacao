#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.




def calcularAnos(populacaoA, populacaoB, crescimentoA, crescimentoB):
    anos = 0
    while(populacaoA < populacaoB):
        populacaoA = populacaoA*(1 + crescimentoA)
        populacaoB = populacaoB*(1 + crescimentoB)
        anos = anos + 1
    return anos


def main():
    populacaoA = 80000
    populacaoB = 200000
    crescimentoA = 0.03
    crescimentoB = 0.015

    print(calcularAnos(populacaoA, populacaoB, crescimentoA, crescimentoB))

# o main só será chamado quando exercutar esse arquivo, dessa forma, podemos reutilizar os métodos desse arquivo
if __name__ == "__main__":
   main()
