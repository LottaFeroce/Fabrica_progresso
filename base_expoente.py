b=int(input("Indique a base: "))
e=int(input("Informe o expoente: "))
p = 1
for o in range(e):
    p*=b
    o+=1
print(b,"^",e,"=",p)
    