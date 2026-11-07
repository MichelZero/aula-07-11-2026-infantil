# 
#
'''
for i in range(3):
  nota1 = int(input(f"informe a nota 1_aluno{i+1}: "))
  nota2 = int(input(f"informe a nota 2_aluno{i+1}: "))
'''

nota1 = 9 # int
preco = 5.4 # float
verdadeiro = True # booleano
palavra = 'texto' # String

lista = [] # lista vazia
# crie uma exemplo te uso de lista 
minha_lista = [1, 2, 3, 4, 5]
print(minha_lista)

# lista de notas
lista_mista = [6, 8, [1, [2], 3], 7.5, 5]


# faça o uso de lista com o for loop
for numero in minha_lista:
    print(numero) 
    
# faça o uso de uma lista com o for loop e a função range()
for i in range(len(minha_lista)):
    print(minha_lista[i])   
    
# adicione um elemento na lista
minha_lista.append(6)
print(minha_lista)

