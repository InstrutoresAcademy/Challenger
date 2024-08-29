import numpy as np
import matplotlib.pyplot as plt

# Definindo as entradas para 20 alunos (horas de estudo e sono)
horas_estudo = np.random.randint(1, 10, size=20)  # Horas de estudo variando de 1 a 10
horas_sono = np.random.randint(1, 10, size=20)  # Horas de sono variando de 1 a 10

# Definindo os pesos e bias
w1 = 0.6
w2 = 0.4
bias = -2

# Calculando a soma ponderada e a saída sigmoide para cada aluno
somas_ponderadas = (w1 * horas_estudo) + (w2 * horas_sono) + bias
saidas_sigmoide = 1 / (1 + np.exp(-somas_ponderadas))

# Imprimindo a soma ponderada e a probabilidade para cada aluno
for i in range(20):
    print(f"Aluno {i+1}: Horas de Estudo = {horas_estudo[i]}, Horas de Sono = {horas_sono[i]}")
    print(f"Soma Ponderada: {somas_ponderadas[i]:.2f}, Probabilidade (Sigmoide): {saidas_sigmoide[i]:.2f}")
    print("-" * 50)

# Gerando uma gama de valores para a soma ponderada (para o gráfico)
x_values = np.linspace(-10, 10, 100)

# Calculando a reta linear e a função sigmoide aplicada aos valores da gama
reta_linear = x_values
curva_sigmoide = 1 / (1 + np.exp(-x_values))

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Plotando a reta da combinação linear (antes da sigmoide)
plt.plot(x_values, reta_linear, label='Reta Linear (Combinação)', color='blue')

# Plotando a curva da função sigmoide
plt.plot(x_values, curva_sigmoide, label='Função Sigmoide', color='red')

# Plotando os pontos dos alunos (soma ponderada e saída sigmoide)
plt.scatter(somas_ponderadas, saidas_sigmoide, color='green', s=100, label='Alunos')

# Adicionando títulos e legendas
plt.title('Gráfico da Reta Linear e Função Sigmoide com Alunos')
plt.xlabel('Soma Ponderada (x)')
plt.ylabel('Valor')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()
