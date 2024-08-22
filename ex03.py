# Crie um programa que permite ao usuário inserir três itens de uma lista de compras. Em seguida, exiba a lista completa.

minha_lista =[]

for i in range(3):
    item = input(f'Informe o {i + 1}° item da lista: ')
    minha_lista.append(item)

print('Lista de compras: ', minha_lista)