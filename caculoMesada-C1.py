#Este projeto tem como objetivo permitir que o usuário insira os valores de sua mesada ao longo de 6 meses, calcular a média dessas mesadas e gerar um gráfico que mostre a variação dos valores ao longo do tempo. O projeto utiliza as bibliotecas Pandas e Matplotlib para manipulação de dados e visualização gráfica
import pandas as pd
import matplotlib.pyplot as plt

# Meses para os quais pediremos as mesadas
# Aqui definimos uma lista com os meses que serão utilizados no projeto.
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']

# Lista para armazenar as mesadas inseridas pelo usuário
# Criamos uma lista vazia para armazenar os valores das mesadas que o usuário irá fornecer.
mesadas = []

# Loop para solicitar as mesadas
# Usamos um loop 'for' para percorrer cada mês da lista 'meses'.
# Em cada iteração, solicitamos ao usuário que insira o valor da mesada para aquele mês.
# O valor inserido é convertido para um número de ponto flutuante (float) e, em seguida, adicionado à lista 'mesadas'.
for mes in meses:
    valor = float(input(f"Digite o valor da mesada para {mes}: R$"))
    mesadas.append(valor)

# Criando o DataFrame com os valores inseridos
# Agora, criamos um dicionário chamado 'dados', onde as chaves são 'Mês' e 'Mesada (R$)'.
# As listas 'meses' e 'mesadas' são atribuídas a essas chaves, respectivamente.
# Em seguida, criamos um DataFrame com esses dados usando a biblioteca Pandas.
dados = {
    'Mês': meses,
    'Mesada (R$)': mesadas
}

df = pd.DataFrame(dados)

# Calculando a média das mesadas
# Utilizando o DataFrame criado, calculamos a média das mesadas com a função 'mean()' aplicada à coluna 'Mesada (R$)'.
# A média é armazenada na variável 'media_mesada'.
# Em seguida, imprimimos a média calculada para o usuário, formatando o valor com duas casas decimais.
media_mesada = df['Mesada (R$)'].mean()
print(f"A média da mesada ao longo dos 6 meses é: R${media_mesada:.2f}")

# Criando o gráfico de linha
# Usamos a biblioteca Matplotlib para criar um gráfico de linha que mostra a variação das mesadas ao longo dos meses.
# A função 'plot()' recebe a lista de meses e a lista de mesadas, e 'marker='o'' adiciona um marcador em cada ponto do gráfico.
# O título do gráfico, assim como os rótulos dos eixos X e Y, são definidos com as funções 'title()', 'xlabel()' e 'ylabel()', respectivamente.
# A função 'grid(True)' adiciona uma grade ao gráfico para facilitar a visualização dos dados.
# Por fim, 'plt.show()' exibe o gráfico gerado na tela.
plt.plot(df['Mês'], df['Mesada (R$)'], marker='o')
plt.title('Variação da Mesada ao Longo dos Meses')
plt.xlabel('Mês')
plt.ylabel('Mesada (R$)')
plt.grid(True)
plt.show()
