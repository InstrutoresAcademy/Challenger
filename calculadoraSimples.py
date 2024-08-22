# Calculadora simples
print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Solicita ao usuário que escolha uma operação
escolha = input("Digite a escolha (1/2/3/4): ")

# Solicita ao usuário que insira dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a operação com base na escolha do usuário
if escolha == '1':
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif escolha == '2':
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif escolha == '3':
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")

elif escolha == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero!")

else:
    print("Escolha inválida!")