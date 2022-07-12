fn=int(input("Digite um número para dar início a sequência: "))
e=int(input("Informe o expoente: "))
f1 = 1
f2 = 0
for t in range(e):
    t = f1 + f2
    f1 = f2
    f2 = t
    print(f2)
   