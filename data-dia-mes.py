ano = int(input("Diga qual ano quer verificar: "))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("Bissexto")
else:
    print("Não é Bissexto")
#365,2425 = 365 + 1  −   1   +   1  
                 # 4     100    400

