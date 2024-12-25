print("Olá! Seja bem vindo ao chatbotLeco\n Digite x se quiser sair do Bot!\n")

nome = input("Qual o seu nome? ")
pergunta = input(f'Olá {nome}, como posso te ajudar hoje? ')

while True:
    print(f'Bot: resposta do BOT')
    pergunta  = input("Usuário:")
    if pergunta.lower() == 'x':
        break

print(f'Obrigado {nome} por ter usado o ChatBotLeco tenha um bom dia!')