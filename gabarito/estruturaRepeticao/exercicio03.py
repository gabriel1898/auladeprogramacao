# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


right = False

while (right == False):
    nota = input("coloque o valor de 0 a 10: ")
    if int(nota) > 10 or int(nota) < 0:
        print("valor invalido")
        certo = False
    else:
        certo = True



def validacaoNome(nome):
    contador = 0
    for x in nome:
        count = count + 1
