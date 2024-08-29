import math
import numpy as np
import matplotlib.pyplot as plt

# Definindo as entradas
# x1 e x2 representam as entradas que o neurônio recebe.
# Essas entradas poderiam ser qualquer característica relevante de um problema real, como dados de sensores ou características de um objeto.
x1 = 0.5
x2 = 0.3

# Definindo os pesos
# w1 e w2 são os pesos associados a cada entrada. Eles determinam a importância de cada entrada na decisão final do neurônio.
# Em um neurônio treinado, esses valores são ajustados para minimizar o erro na saída.
w1 = 0.4
w2 = 0.7

# Definindo o bias
# O bias é um valor constante adicionado à soma ponderada das entradas. Ele permite que o neurônio faça ajustes finos na saída, mesmo quando as entradas são zero.
bias = -0.2

# Calculando a soma ponderada das entradas
# A soma ponderada é calculada multiplicando cada entrada pelo seu respectivo peso, somando os resultados, e adicionando o bias.
# Este é o primeiro passo no processamento de um neurônio.
soma_ponderada = (w1 * x1) + (w2 * x2) + bias
print(f"Soma Ponderada: {soma_ponderada}")

# Definindo a função sigmoide
# A função sigmoide é uma função de ativação que transforma a soma ponderada em uma saída entre 0 e 1.
# Ela é frequentemente usada em tarefas de classificação binária, onde a saída precisa ser interpretada como uma probabilidade.
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Aplicando a função de ativação
# A saída do neurônio é obtida aplicando a função sigmoide à soma ponderada.
# Esta saída é uma probabilidade que reflete a "ativação" do neurônio.
saida = sigmoid(soma_ponderada)
print(f"Saída do Neurônio: {saida}")

# Gerando uma gama de valores para a soma ponderada
# Aqui, criamos um conjunto de valores de soma ponderada entre -10 e 10 para visualizar como a função sigmoide se comporta.
x_values = np.linspace(-10, 10, 100)

# Calculando os pontos mapeados (soma ponderada sem aplicar a sigmoide)
# Os pontos mapeados são os valores da soma ponderada antes de passar pela função sigmoide.
somas_ponderadas = x_values  # Esses são os valores antes da função sigmoide

# Aplicando a função sigmoide a esses valores
# Para cada valor da soma ponderada, calculamos a saída correspondente usando a função sigmoide.
saidas_sigmoide = sigmoid(x_values)

# Gráfico 1: Pontos Mapeados
# O primeiro gráfico mostra os pontos mapeados, ou seja, as somas ponderadas geradas acima.
# Isso nos permite ver como as somas ponderadas se distribuem antes de qualquer transformação pela função sigmoide.
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(x_values, somas_ponderadas, color='blue')
plt.title('Pontos Mapeados (Soma Ponderada)')
plt.xlabel('Entradas Combinadas')
plt.ylabel('Soma Ponderada')
plt.grid(True)

# Gráfico 2: Função Sigmoide Aplicada
# O segundo gráfico mostra como a função sigmoide transforma essas somas ponderadas em saídas entre 0 e 1.
# Isso ilustra como a sigmoide "comprime" qualquer valor real da soma ponderada para o intervalo [0, 1].
plt.subplot(1, 2, 2)
plt.plot(x_values, saidas_sigmoide, color='red')
plt.title('Função Sigmoide Aplicada')
plt.xlabel('Soma Ponderada')
plt.ylabel('Saída Sigmoide')
plt.grid(True)

# Exibindo os gráficos
# Usamos tight_layout() para garantir que os subplots fiquem bem organizados, sem sobreposição de textos e elementos.
plt.tight_layout()
plt.show()
#teste