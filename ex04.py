# Peça ao usuário para inserir cinco palavras, uma de cada vez. Adicione-as a uma lista e depois exiba o primeiro e o último elemento.

palavras = []

for i in range(5):
    palavra = input(f'Informe a {i+1}° palavra: ')
    palavras.append(palavra)

print(f'A primeira palavra informada foi: {palavras[0]}')

print(f'A última palavra informada foi: {palavras[-1]}')