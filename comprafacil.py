print("Digite os Itens no seu carrinho de compras")
preco1 = int(input("Digite o preço do item 1: "))
preco2 = int(input("Digite o preço do item 2: "))
preco3 = int(input("Digite o preço do item 3: "))
if preco1 < preco2 and preco1 < preco3:
    print("Você deve comprar este item: ",preco1,"R$")
elif preco2 < preco1 and preco2 < preco3:
    print("Você deve comprar este item: ",preco2,"R$")
elif preco3 < preco2 and preco3 < preco1:
    print("Você deve comprar este item: ",preco3,"R$")


