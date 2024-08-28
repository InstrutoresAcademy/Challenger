import matplotlib.pyplot as plt  # Biblioteca para criar gráficos
import pandas as pd  # Biblioteca para manipulação de dados em DataFrames
import smtplib  # Biblioteca para envio de e-mails via protocolo SMTP
from email.mime.multipart import MIMEMultipart  # Classe para criar mensagens de e-mail com múltiplas partes
from email.mime.text import MIMEText  # Classe para criar o corpo do e-mail em texto simples
from email.mime.base import MIMEBase  # Classe para anexar arquivos ao e-mail
from email import encoders  # Biblioteca para codificação dos anexos em base64

def calcular_imposto(renda):
    if renda <= 27110.4:
        imposto = 0.0
    elif renda <= 33919.8:
        imposto = (renda * 0.075) - 169.44
    elif renda <= 45012.6:
        imposto = (renda * 0.15) - 381.44
    elif renda <= 55976.16:
        imposto = (renda * 0.225) - 662.77
    else:
        imposto = (renda * 0.275) - 896.00
    
    # Garantir que o imposto não seja negativo
    if imposto < 0:
        imposto = 0.0

    return imposto

# Função para gerar o gráfico do imposto de renda por membro da família
def gerar_grafico_imposto_familia(nome_familia, entradas):
    df = pd.DataFrame(entradas)  # Converte a lista de entradas em um DataFrame do pandas
    total_imposto = df['Imposto Pago'].sum()  # Calcula o total de imposto pago pela família

    plt.figure(figsize=(10, 6))  # Configura o tamanho do gráfico
    barras = plt.bar(df['Nome'], df['Imposto Pago'], color='green')  # Cria o gráfico de barras
    plt.xlabel('Membro da Família')  # Define o rótulo do eixo X
    plt.ylabel('Imposto Pago (R$)')  # Define o rótulo do eixo Y
    plt.title(f'Imposto Pago por Membro da Família {nome_familia} (Total: R$ {total_imposto:.2f})')  # Define o título do gráfico
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo X para facilitar a leitura
    plt.tight_layout()  # Ajusta o layout para que todos os elementos caibam bem no gráfico

    # Adiciona os valores pagos acima de cada barra no gráfico
    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2.0, altura, f'R$ {altura:.2f}', ha='center', va='bottom')

    # Salva o gráfico como um arquivo PNG
    plt.savefig(f'grafico_imposto_familia_{nome_familia.lower()}.png')
    print(f"Gráfico gerado e salvo como 'grafico_imposto_familia_{nome_familia.lower()}.png'.")

# Função para enviar o gráfico gerado por e-mail
def enviar_email(nome_familia, destinatario_email):
    remetente = 'innova@example.com'  # E-mail do remetente
    senha = 'sua senha'  # Senha ou senha de aplicativo do remetente

    # Configura a mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario_email  # Define o destinatário do e-mail
    msg['Subject'] = f'Relatório de Imposto de Renda da Família {nome_familia}'  # Define o assunto do e-mail

    # Corpo do e-mail
    corpo = f'Prezados,\n\nSegue em anexo o relatório de Imposto de Renda da Família {nome_familia.upper()}.\n\nAtenciosamente,\nInnova Academy'
    msg.attach(MIMEText(corpo, 'plain'))  # Anexa o corpo do e-mail em texto simples

    # Anexar o gráfico gerado ao e-mail
    nome_arquivo = f'grafico_imposto_familia_{nome_familia.upper()}.png'
    anexo = open(nome_arquivo, 'rb')  # Abre o arquivo em modo de leitura binária
    parte = MIMEBase('application', 'octet-stream')
    parte.set_payload(anexo.read())  # Lê o conteúdo do arquivo
    encoders.encode_base64(parte)  # Codifica o arquivo em base64 para envio
    parte.add_header('Content-Disposition', f'attachment; filename={nome_arquivo}')  # Adiciona o cabeçalho de anexo ao e-mail
    msg.attach(parte)  # Anexa o arquivo ao e-mail

    # Enviar o e-mail via SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Conecta ao servidor SMTP do Gmail
    server.starttls()  # Inicia a comunicação criptografada
    server.login(remetente, senha)  # Faz login no servidor SMTP com as credenciais do remetente
    texto = msg.as_string()  # Converte a mensagem em string para envio
    server.sendmail(remetente, destinatario_email, texto)  # Envia o e-mail para o destinatário
    server.quit()  # Encerra a conexão com o servidor SMTP

    print(f"E-mail enviado com sucesso para {destinatario_email}!")  # Confirmação de envio de e-mail

# Função principal do script
if __name__ == "__main__":
    entradas = []  # Lista para armazenar os dados dos membros da família
    nome_familia = input("Informe o nome da família: ")  # Solicita o nome da família

    while True:  # Loop para entrada dos dados dos membros da família
        nome = input("Informe o nome do membro da família (ou digite 'sair' para finalizar): ")  # Solicita o nome do membro
        if nome.lower() == 'sair':
            break  # Sai do loop se o usuário digitar 'sair'

        renda_anual = float(input(f"Informe a renda anual de {nome}: R$ "))  # Solicita a renda anual do membro
        imposto_a_pagar = calcular_imposto(renda_anual)  # Calcula o imposto a pagar para o membro
        print(f"O valor do imposto de renda a ser pago por {nome} é: R$ {imposto_a_pagar:.2f}")

        # Adiciona os dados do membro à lista de entradas
        entradas.append({'Nome': nome, 'Renda Anual': renda_anual, 'Imposto Pago': imposto_a_pagar})

    if entradas:  # Se houver membros na lista, gera o gráfico
        gerar_grafico_imposto_familia(nome_familia, entradas)

        # Pergunta se deseja enviar o gráfico por e-mail
        enviar = input("Deseja enviar o gráfico por e-mail? (s/n): ")
        if enviar.lower() == 's':
            destinatario = input("Informe o e-mail do destinatário: ")  # Solicita o e-mail do destinatário
            enviar_email(nome_familia, destinatario)  # Envia o gráfico por e-mail