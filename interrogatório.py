print("Por favor responda com: Sim ou Não")
fone = input("Telefonou para a vítima? ")
loc = input("Esteve no local do crime? ")
mora = input("Mora perto da vítima? ")
deve = input("Devia para a vítima? ")
trab = input("Já trabalhou com a vítima? ")
count = 0
if fone == 'Sim' or fone == 'sim':
    count +=1
if loc == 'Sim' or loc == 'sim':
    count +=1
if mora == 'Sim' or mora == 'sim':
    count +=1
if deve == 'Sim' or deve == 'sim':
    count +=1
if trab == 'Sim' or trab == 'sim':
    count +=1

if count == 2:
    print("SUSpeito")
elif count == 3 or count == 4:
    print("Cúmplice")
elif count == 5:
    print("Assasino")
else:
    print("Inocente")
    
