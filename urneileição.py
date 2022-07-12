c1 = 1
c2 = 2
c3 = 3
c4 = 4
nulo = 5
bc = 6
votot = 0
#total de votos por candidato, total de votos nulos e total de votos brancos.
print("Seja bem-vindo(a) às eleições 2022.")
print("Informe o seu candidato utilizando 1|2|3|4 para seus respectivos candidatos.","\n5 Para nulo, 6 Para branco e 0 para finalizar")
while True:
    voto = int(input("Digite o seu voto: "))
    if voto == 0:
        print("Votação concluida")
        break
    if voto == 1:
        print("Seu voto foi para o candidato 1")
    if voto == 2:
        print("Seu voto foi para o candidato 2")
    if voto == 3:
        print("Seu voto foi para o candidato 3")
    if voto == 4:
        print("Seu voto foi para o candidato 4")
    if voto == 5:
        print("Seu voto foi nulo")
    if voto == 6:
        print("Seu voto foi branco")