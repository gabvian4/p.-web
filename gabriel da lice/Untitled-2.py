numfinal=int(input("digite um número inteiro: "))
numinicial=2
lista=[]
while numinicial < numfinal:
    lista.append(numinicial)
    numinicial +=1
for num in lista:
    if num % 2 == 0:
        print(num)

