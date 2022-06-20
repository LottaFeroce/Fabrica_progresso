a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
if (a==0):
    print("O valor de A foi igual a zero por tanto a equação não é do segundo grau.")
else:
    dlt = (b**2) - 4*a*c
    print("Delta é igual a: ",dlt)
    dlt = (b**2) - 4*a*c
    if dlt<0:
        print("O valor de Delta foi menor que zero. resultando em raizes imaginarias")
    elif (dlt==0):
            r = -b/ (2*a)
            print("Possui apenas uma raiz real: ",r)
    else:
        r1 = (-b + (dlt**2) / (2*a))
        r2 = (-b - (dlt**2) / (2*a))
        print("Existem duas raizes reais: ","%.0f" % r1,"e","%.0f" % r2)

