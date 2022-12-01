# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

n1 = int(input("\nDigite o primeiro número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
n4 = int(input("Digite outro número: "))
n5 = int(input("Digite outro número: "))
n6 = int(input("Digite outro número: "))
n7 = int(input("Digite outro número: "))
n8 = int(input("Digite outro número: "))
n9 = int(input("Digite outro número: "))
n10 = int(input("Digite outro número: "))
list1 = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

par = 0
impar = 0

for value in list1:
    if value % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print("Par: ", par, "\nImpar: ", impar)