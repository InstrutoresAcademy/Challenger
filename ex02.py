# crie um programa que pergunta um nome e imprime uma saudação com aquele nome, até que a palavra "sair" seja digitada

nome = ""

while nome != "sair":
    nome = input("Digite seu nome (ou 'sair' para encerrar): ")
    if nome != "sair":
        print(f"Olá, {nome}!")
  
print("Programa encerrado.")
