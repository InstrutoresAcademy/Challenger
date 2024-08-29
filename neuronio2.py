# Definição das Entradas:
# As entradas (x1, x2) representam as características relevantes para a decisão do neurônio.
# Exemplo: x1 = 5 (horas estudadas), x2 = 7 (horas de sono).

# Definição dos Pesos:
# Os pesos (w1, w2) determinam a importância relativa de cada entrada na decisão final.
# Exemplo: w1 = 0.6, w2 = 0.4.

# Adição do Bias:
# O bias é um valor constante que permite ao neurônio ajustar a soma ponderada.
# Exemplo: bias = -2.

# Cálculo da Soma Ponderada:
# A soma ponderada é calculada como a combinação linear das entradas multiplicadas pelos seus respectivos pesos, mais o bias.
# Fórmula: soma_ponderada = (w1 * x1) + (w2 * x2) + bias.
# A soma ponderada é impressa para verificação.

# Implementação da Função de Ativação (Sigmoide):
# A função sigmoide transforma a soma ponderada em um valor entre 0 e 1, que pode ser interpretado como uma probabilidade.
# Fórmula: sigmoid(x) = 1 / (1 + np.exp(-x)).
# A função sigmoide é aplicada à soma ponderada e a saída é impressa.

# Visualização com Gráfico:
# Geração de Valores: Geração de uma gama de valores para a soma ponderada.
# Plotagem da Reta Linear: A reta azul representa a combinação linear das entradas.
# Plotagem da Curva Sigmoide: A curva vermelha mostra como a sigmoide transforma a soma ponderada.
# Destacar o Ponto Específico: O ponto verde destaca a soma ponderada específica e sua transformação pela sigmoide.
# Exibição do Gráfico: O gráfico é exibido com todas essas informações, mostrando como a soma ponderada é mapeada para uma probabilidade.

# Discussão:
# Impacto dos Pesos e Bias: Como a alteração dos pesos e do bias afeta a saída do neurônio.
# Interpretação: A importância da função sigmoide em normalizar a saída para um intervalo interpretável.

import math
import numpy as np
import matplotlib.pyplot as plt

# Definindo as entradas
x1 = 5  # Número de horas estudadas
x2 = 7  # Número de horas de sono

# Definindo os pesos iniciais
w1 = 0.6
w2 = 0.4

# Definindo o bias inicial
bias = -2

# Calculando a soma ponderada das entradas
soma_ponderada = (w1 * x1) + (w2 * x2) + bias
print(f"Soma Ponderada: {soma_ponderada}")
# Definindo a função sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Aplicando a função de ativação
saida = sigmoid(soma_ponderada)
print(f"Saída do Neurônio (Probabilidade): {saida}")

# Gerando uma gama de valores para a soma ponderada
x_values = np.linspace(-10, 10, 100)

# Calculando a função linear e a sigmoide aplicada
somas_ponderadas = x_values  # Esses são os valores antes da função sigmoide
saidas_sigmoide = sigmoid(x_values)

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Plotando a reta da combinação linear (antes da sigmoide)
plt.plot(x_values, somas_ponderadas, label='Reta Linear (Combinação)', color='blue')

# Plotando a curva da função sigmoide
plt.plot(x_values, saidas_sigmoide, label='Função Sigmoide', color='red')

# Destacando o ponto da soma ponderada e sua saída pela sigmoide
plt.scatter([soma_ponderada], [saida], color='green', s=100, label=f'Ponto: ({soma_ponderada:.2f}, {saida:.2f})')

# Adicionando títulos e legendas
plt.title('Gráfico da Reta Linear e Função Sigmoide')
plt.xlabel('Soma Ponderada (x)')
plt.ylabel('Valor')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()
