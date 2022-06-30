popua = int(input("Digite o número de residentes da população A: "))
popub = int(input("Digite o número de residentes da população B: "))
t = 0
while popua < 0 or popub < 0:
    print("Não existe valor negativo de população")
    if popua < 0:
        popua = int(input("Informe o número real de residentes da população A: "))
    elif popub < 0:
        popub = int(input("Informe o número real de residentes da população B: "))
while popua <= popub:
    popua += popua * 0.03
    popub += popub * 0.015
    t += 1
print("A população a ultrapassou a b em :",t,"Anos")