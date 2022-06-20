turno = (input("Digite o seu Gênero: "))
if turno.isalpha():
    if turno == 'M' or turno == 'm':
        print("Bom Dia")
    elif turno == 'V' or turno == 'v':
        print("Boa Tarde")
    elif turno == 'N' or turno == 'n':
        print("Boa Noite")
    else: print("Opção inexistente")
else: print("Digite o turno em letras")
8