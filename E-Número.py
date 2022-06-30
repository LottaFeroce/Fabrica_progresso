num = int(input("Digite um número entre zero e dez: "))
while num < 0 or num >10:
    print("Informe um valor válido")
    num = int(input("Digite o valor correto: "))
print("O valor foi:",num)