# 2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

print('############### CADASTRO PESSOAL ###############')

print ("Faça o seu cadastro: ")
usuario = str(input("usuário--> "))
senha = str(input("senha--> "))
while usuario==senha:
	print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	usuario = str(input("usuário--> "))
	senha = str(input("senha--> "))
else:
	print("Cadastrado efetuado com sucesso")