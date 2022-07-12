#Em termos matemáticos, a sequência é definida pela fórmula Fn = fn-1 + Fn-2,
#sendo o  primeiro termo F1= 1 e os valores iniciais F1 = 1, F2 =1.
fn=int(input("Digite um número para dar início a sequência: "))
f1 = 1
f2 = 0
for t in range(1,18):
    t = f1 + f2
    f1 = f2
    f2 = t
    print(f2)