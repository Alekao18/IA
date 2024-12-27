def respostas_bot(mensagens):
    return 'Resposta BOT'


print("Olá! Seja bem vindo ao chatbotLeco\n Digite x se quiser sair do Bot!\n")

nome = input("Qual o seu nome? ")

mensagens = []

while True:
    pergunta  = input("Usuário:")
    if pergunta.lower() == 'x':
        break
    mensagens.append({'role':'user', 'content': pergunta})
    resposta = respostas_bot(mensagens)
    mensagens.append({'role':'bot', 'content': resposta})
    print(f'Bot: {resposta}')

print(f'Obrigado {nome} por ter usado o ChatBotLeco tenha um bom dia!')
print(f'Nosso histório de mensagens foi: {mensagens}')

'''
FUNÇÃO:
def soma(a, b):
    return a+b
soma(1,2)
print(soma)'''