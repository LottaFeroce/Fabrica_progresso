nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
sal = float(input("Digite o valor do seu salário: "))
sex = input("Digite o seu gênero com (F para Feminino, M para Masculino e o para outro): ")
ec = input("Digite o seu estado civil com (s para solteiro, c para casado e v para viuvo): ")
while len(nome) <= 3:
    print("O nome precisa ter mais de três caracteres")
while idade <0 and idade >150:
    print("Informe uma idade valida")
while sal <0:
    print("Consulte o agiota mais proximo: ")
while sex != "f" or sex != "F" and sex != "m" or sex != "M" and sex != "o" or sex != "O":
    print("Gênero erradão em")
while ec != "s" or ec != "S" and ec != "c" or ec != "C" and ec != "v" or ec != "V":
    print("A informação é invalida")
    
