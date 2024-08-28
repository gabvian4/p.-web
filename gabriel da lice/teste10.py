lista1=[]
lista2=[]
for i in range(4):
    lista1.append(input("digite um numero: "))
for i in range(4):
    lista2.append(input("digite outro numero:  "))
result= lista1 + lista2
result= list(set(result))
result= (sorted(result))
#print(resultado)
print('\n'.join(map(str, result)))
print("fim de programa")
