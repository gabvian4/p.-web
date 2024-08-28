import random
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
I = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
N = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
G = [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
O = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
letras=["B", "I", "N", "G", "O"]
num_sorteio=str(input("sortear um numero?"))
num_usados=[]
while num_sorteio=="s" or num_sorteio=="n":
    letra=random.choice(letras)
    if letra== "B":
        num_sorteio=random.choice(B)
        while num_sorteio in num_usados:
            print("esse num ja foki sorteado. vamos sortear outros...")
            num_sorteio=random.choice(B)
        num_usados.append(num_sorteio)
        print("a letra sorteada foi: ", {letra}, "e o num foi: ", {num_sorteio})
        sorteio=str(input("sortear outro num?"))
    if letra== "I":
        num_sorteio=random.choice(I)
        while num_sorteio in num_usados:
            print("a letra sorteada foi: ", {letra}, "e o num foi: ", {num_sorteio})
            num_sorteio=random.choice(I)
        num_usados.append(num_sorteio)
        print("a letra sorteada foi: , e o num foi: ")
        sorteio=str(input("sortear outro num?"))
    if letra== "N":
        num_sorteio=random.choice(N)
        while num_sorteio in num_usados:
            print("esse num ja foi sorteado. vamos sortear outros...")
            num_sorteio=random.choice(N)
        num_usados.append(num_sorteio)
        print("a letra sorteada foi: ", {letra}, "e o num foi: ", {num_sorteio})
        sorteio=str(input("sortear outro num?"))
    if letra== "G":
        num_sorteio=random.choice(G)
        while num_sorteio in num_usados:
            print("esse num ja foi sorteado. vamos sortear outros...")
            num_sorteio=random.choice(G)
        num_usados.append(num_sorteio)
        print("a letra sorteada foi: ", {letra}, "e o num foi: ", {num_sorteio})
        sorteio=str(input("sortear outro num?"))
    if letra== "O":
        num_sorteio=random.choice(O)
        while num_sorteio in num_usados:
            print("esse num ja foki sorteado. vamos sortear outros...")
            num_sorteio=random.choice(O)
        num_usados.append(num_sorteio)
        print("a letra sorteada foi: ", {letra}, "e o num foi: ", {num_sorteio})
        sorteio=str(input("sortear outro num?"))
        print("fim de programa")
