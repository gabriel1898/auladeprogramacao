#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.



# método para ir de letra em letra na palavra e transforma-la numa lista de letras
def splitString(word):
    return [x for x in word]

def checkEqual(word1, word2):
    #loop para mover de caractere em caractere na palavra
    for x in word1:
        if x != word2[word1.index(x)]:
            print("operação bem sucedida")
            igual = False
            break
    else:
        igual = True
        print("o login é igual à senha, mude um dos dois")
    return igual



#variável para avaliar se deve voltar a pedir a senha e o login (caso sejam iguais)
igual = True


while (igual == True):
    #pede login e senha do usuário
    login = input("login: ")
    password = input("password: ")

    #transforma string em lista
    login = splitString(login)
    password = splitString(password)

    igual = checkEqual(login, password)



