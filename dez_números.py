#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
#pares e a quantidade de números ímpares.
'''n=int(input("Informe dez números: "))
c = 1
for p in range (1,11):
    print(p)
    if p == 11:
     continue
    if (p%2) == 0:
        print("\nPar")
        c=+1
    else:
        print("\nImpar")
        c =+1
print(c)'''
p = 0
i = 0
for c in range (10):
    if int(input("Digite um número: ")) %2 == 0:
        p +=1
    else:
        i += 1
print("Pares:",p,"\nImpares:",i)