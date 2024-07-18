import random
a=ramdom.randit(1,1000)
cont=1
valor=0
while cont==1:
    b=int(input("digite um num de 1 a 1000: "))
    if a<b:
        print("num sorteado é menor que esse")
        valor+=1
    elif a>b:
        print("num sorteado é maior que esse")
        valor+=1
    elif a==b:
        print("você acertou!!usando essas alternativas:" ,valor)
