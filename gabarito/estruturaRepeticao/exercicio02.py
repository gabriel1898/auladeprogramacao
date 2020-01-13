#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.



# método para ir de letra em letra na palavra e transforma-la numa lista de letras
def splitString(word):
    return [x for x in word]




#pede login e senha do usuário
login = input("login: ")
password = input("password: ")

loginChar = splitString(login)
passwordChar = splitString(password)

print(loginChar, passwordChar)



