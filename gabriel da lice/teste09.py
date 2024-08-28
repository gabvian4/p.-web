lista=[]
outralista= []
for i in range(4):
    valores=int(input("digite um numero inteiro: "))
    if valores >=15 and valores <=30:
        lista.append(valores)
    elif valores not in lista and valores >=1 and valores <=50:
        outralista. append(valores)
soma=sum(lista)
print("a somas dos numeros  entre 15 e 30 é: ", soma)
print("os valores na lista são: ", lista)