while True:
    nota = float(input("Informe uma nota entre zero e dez: "))
    if nota <0 or nota >10:
        print("Informe um valor válido")
    else:
        print("A nota foi: ",nota)
    break
