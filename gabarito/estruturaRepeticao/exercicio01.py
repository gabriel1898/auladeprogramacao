# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


certo = False

while (certo == False):
    nota = input("coloque o valor de 0 a 10: ")
    if int(nota) > 10 or int(nota) < 0:
        print("valor invalido")
        certo = False
    else:
        certo = True

