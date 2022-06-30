nota1 = float(input("Informe a sua nota: "))
nota2 = float(input("Informe a sua nota: "))
mediap = (nota1+nota2)/2
print("A média parcial foi: ",mediap)
if mediap >= 9.0 or mediap == 10:
    print("Classificação A")
elif mediap >= 7.5 or mediap == 9.0:
    print("Classificação B")
elif mediap >= 6.0 or mediap == 7.5:
    print("Classificação C")
elif mediap >= 4.0 or mediap == 6.0:
    print("Classificação D")
elif mediap >= 4.0 or mediap == 0:
    print("Classificação E")
