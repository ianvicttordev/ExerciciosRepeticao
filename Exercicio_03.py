# 3 - Faça um programa que leia e valide as seguintes informações:
# A - Nome: maior que 3 caracteres;
# B - Idade: entre 0 e 150;
# C - Salário: maior que zero;
# D - Sexo: 'f' ou 'm';
# E - Estado Civil: 's', 'c', 'v', 'd';

#Nome: maior que 3 caracteres;

nome = input("Informe um nome--> ")
while (len(nome) <=  3):
	nome = str(input("Informe um nome--> "))

#Idade: entre 0 e 150;

idade = int(input("Informe a idade--> "))
while (idade > 150 and idade < 0):
	idade = int(input("Informe a idade--> "))
	
	
#Salário: maior que zero;
salario = float(input("Informe um salário--> "))
while (salario < 0):
	salario = float(input("Informe um salário--> "))
	
#Sexo: 'f' ou 'm';

sexo = str(input("Informe a inicial do seu sexo--> "))
while  sexo !="f" and sexo!="m" :
	sexo = input("Informe a inicial do seu sexo--> ")
	
#Estado Civil: 's', 'c', 'v', 'd';

estado_civil = str(input("Informe a inicial do seu estado civil-->"))
while (estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
	estado_civil = input("Informe a inicial do seu estado civil--> ")