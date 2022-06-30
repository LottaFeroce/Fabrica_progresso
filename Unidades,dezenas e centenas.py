num = int(input("Afirme um número menor que mil: "))
uni = num % 10
num = (num - uni)/10
deze = num % 10
num = (num - deze)/10
cent = num
deze = int(deze)
cent = int(cent)
print(cent,"Centenas\n",deze,"Dezenas\n",uni,"Unidades")
