angulo1 = float(input("Digite um valor: "))
angulo2 = float(input("Digite um valor: "))
angulo3 = float(input("Digite um valor: "))
if (angulo1 +  angulo2 < angulo3) or (angulo1 +  angulo3 < angulo2) or (angulo2 +  angulo3 < angulo1) :
    print("É um Triangulo classico")
elif (angulo1 == angulo2) and (angulo1 == angulo3):
    print("É um Triangulo Equilatero")
elif (angulo1 == angulo2) or (angulo3 == angulo1):
    print("É um Triangulo Isósceles")
else:
    print("É um Triangulo Escaleno")
