while True:
    p1 = float(input("Informe o valor do produto 1: "))
    p2 = float(input("Informe o valor do produto 2: "))
    p3 = float(input("Informe o valor do produto 3: "))
    total = p1 + p2 + p3
    din = float(input("R$ fornecidos: "))
    troco = din-total
    print("O valor do produto 1:",p1,"\nO valor do produto 2:",p2,"\nO valor do produto 3:",p3,"\nO total:",total,"\nDinehiro fornecido:",din,"\nTotal do troco:",troco)
    opera = int(input("Finalizar compra? 1-Não e 0-Sim: "))
    if opera == 0:
        print("Compra finalizada")
        break
