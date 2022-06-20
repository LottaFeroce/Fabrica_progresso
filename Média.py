nota1 = int(input("Digite a primeira Nota: "))
nota2 = int(input("Digite a segunda Nota: "))
media = (nota1+nota2)/2
if media >=7 : #Limite da aprovação
    print("Aprovado")
elif media <=5 :
    print("Reprovado")
elif media == 10:
    print("Aprovado Sem Distinção")
