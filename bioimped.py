print("Bem-vindo ao sistema Bioimpedico do Draven. insira seus dados abaixo")
nome = (input("Digite o seu nome: "))
idade = float(input("Digite a sua idade: "))
endereco = (input("Digite o seu endereço: "))
fone = (input("Digite o seu telefone: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = (peso/(altura**altura))
massag = (1.20 * imc) + (0.23 *idade) - (10.8 * 1) - 5.4
massam = (1.20 * imc) - massag
aguac = (peso * 35)
aguaL = (aguac/1000)
maza = (peso/altura**2)
#O peso residual corresponde ao peso dos componentes corporais, excluindo gordura, músculos e ossos.
gordv = float(input("Digite a circunferência do quadril(cm): "))
iac = (gordv/altura**1.5) - 18
tpulso = float(input("Digite o diametro do pulso do paciente: "))
tfemur = float(input("Digite o diametro do femur do paciente: "))
pesoosse = (altura * tfemur / tpulso)
print("%.2f" % pesoosse,"Kg","Peso Ósseo")
print(aguac,"Ml")
print(aguaL,"L")
print("%.2f" % massag,"Kg","Massa Gorda")
print("%.2f" % massam,"Kg","Massa Magra")
print("%.2f" % imc,"IMC")
print("%.2f" % iac,"Kg","Gordura Visceral(IAC)")
print("%.2f" % maza,"Kg","Massa muscular")
if imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Acima do peso(sobrepeso)")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade I")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade II")
elif imc > 40:
    print("Obesidade III")
