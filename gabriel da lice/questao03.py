#Questão 01: Combinação de Cursos:
#Duas faculdades oferecem cursos diferentes. A Faculdade A oferece
#["Matemática", "Física", "Biologia"] e a Faculdade B oferece ["Biologia",
#"Química", "Filosofia"]. Escreva um algoritmo que combine essas listas,
#eliminando duplicatas, para criar uma lista de todos os cursos oferecidos.

cursos1=[]
cursos2=[]
for i in range(3):
    cursos1.append(input("digite uma materia: "))
for i in range(3):
    cursos2.append(input("digite outra materia: "))
result= cursos1 + cursos2
result= list(set(result))
result= (sorted(result))
#print(resultado)
print('\n'.join(map(str, result)))
print("fim de programa")

#Questão 02: Atualização de Contatos:
#você tem duas listas de contatos, uma no seu telefone ["Alice", "Bruno",
#"Carlos"] e outra no seu e-mail ["Carlos", "Diana", "Eduardo"]. Crie uma lista
#única de todos os contatos para sincronizar com um novo dispositivo.

lista1=[]
lista2=[]
for i in range(3):
    lista1.append(input("digite três nome no seu contato: "))
for i in range(3):
    lista2.append(input("digite outros três nomes: "))
result= lista1 + lista2
result= list(set(result))
result= (sorted(result))
#print(resultado)
print('\n'.join(map(str, result)))
print("fim de programa")



#Questão 07: Unificação de Catálogos de Livros:
#Uma livraria está unificando os catálogos de duas filiais. O catálogo da Filial A
#contém os livros ["O Senhor dos Anéis", "1984", "Dom Casmurro"], e o da Filial
#B contém ["Dom Casmurro", "O Pequeno Príncipe", "1984"]. Escreva um
#algoritmo que crie um catálogo único, sem duplicatas, de todos os livros
#disponíveis nas duas filiais.

lista1=["O Senhor dos Anéis", "1984", "Dom Casmurro"]
lista2=["Dom Casmurro", "O Pequeno Príncipe", "1984"]
result= lista1 + lista2
result= list(set(result))
result= (sorted(result))
#print(resultado)
print('\n'.join(map(str, result)))
print(f" catálogo único, sem duplicatas, de todos os livros  disponíveis nas duas filiais {result}")
