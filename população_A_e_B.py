popua = 80000
popub = 200000
t = 0
while popua <= popub:
    popua += popua * 0.03
    popub += popub * 0.015
    t += 1
print("A população a ultrapassou a b em :",t,"Anos")