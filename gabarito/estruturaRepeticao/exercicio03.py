# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';



def validarNome(nome):
    if len(nome) >= 3:
        return True
    else:
        return False


def validarIdade(idade):
    if idade >= 0 and idade <= 150:
        return True
    else:
        return False

def validarSalario(salario):
    if salario > 0:
        return True
    else:
        return False

def validarSexo(sexo):
    if sexo == 'f' or sexo == 'm':
        return True
    else:
        return False

def validarEstadoCivil(estadoCivil):
    if estadoCivil == 's' or estadoCivil == 'c' or estadoCivil == 'v' or estadoCivil == 'd':
        return True
    else:
        return False


def main():

    validacaoNome = False
    validacaoIdade = False
    validacaoSalario = False
    validacaoSexo = False
    validacaoEstadoCivil = False
    while(validacaoNome == False):
        nome = input("coloque seu nome: ")
        if validarNome(nome) == True:
            break
        print("nome invalido, insira novamente")


    while(validacaoNome == False):
        idade = input("coloque sua idade: ")
        if validarIdade(int(idade)) == True:
            break
        print("idade invalido, insira novamente")


    while(validacaoSalario == False):
        salario = input("coloque seu salario: ")
        if validarSalario(int(salario)) == True:
            break
        print("salario invalido, insira novamente")

    while(validacaoSexo == False):
        sexo = input("coloque seu sexo [f ou m]: ")
        if validarSexo(sexo) == True:
            break
        print("sexo invalido, insira novamente")

    while(validacaoEstadoCivil == False):
        estadoCivil = input("coloque seu estado civil [s, c, d ou v]: ")
        if validarEstadoCivil(estadoCivil) == True:
            break
        print("estado civil invalido, insira novamente")



# o main só será chamado quando exercutar esse arquivo, dessa forma, podemos reutilizar os métodos desse arquivo
if __name__ == "__main__":
   main()


