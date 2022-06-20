a = "snooping as usual i see"
a.capitalize()
print(a)
a.casefold()
print(a)
b = ("s","23","n22m",3523343)
print(b)
c = tuple(["larry","35","90kg",1980.2003])#Deeznuts
print(c)
print(type(a))
print(type(b))
print(type(c))
print(len(c))
d = ("squidward","on","a","Chair")
print(d[0])

bestsellers= ("Call of Chtulhu","The Chalkman","The King in Yellow")
print("Call of Chtulhu" in bestsellers)
print(bestsellers.index("The King in Yellow"))
if"The Rake" in bestsellers:
    print(bestsellers.index("The Rake"))
else:
    print("The Rake não está na tupla")
