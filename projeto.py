import os #biblioteca do sistema operacional
from langchain_groq import ChatGroq 
from langchain.prompts import ChatPromptTemplate

api_key = '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'
os.environ ['GROQ_API_KEY'] = api_key # variável de ambiente
chat = ChatGroq(model = 'llama-3.3-70b-versatile') 

def respostas_bot(mensagens, documento):
    mensagem_system = '''Você é um assistente amigávelque se chama Leco.
    Você tem acesso as seguintes {informacoes}'''
    mensagens_modelo = [('system', mensagem_system)]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import PyPDFLoader

def carrega_sites():
    url = input("Coloque aqui a url do site: ")
    loader = WebBaseLoader(url) 
    lista_documentos = loader.load()
    documentos= ''
    for doc in lista_documentos:
        documentos += doc.page_content
    return documentos

def carrega_youtube():
    url = input("Coloque aqui o seu video:")
    loader = YoutubeLoader.from_youtube_url(url, language = 'pt')
    lista_yt = loader.load()
    documentos= ''
    for doc in lista_yt:
        documentos += doc.page_content
    return documentos

def carrega_pdf():
    caminho = input("Coloque aqui o seu pdf:")
    loader = PyPDFLoader(caminho)
    lista_pdf = loader.load()
    documentos= ''
    for doc in lista_pdf:
        documentos += doc.page_content
    return documentos

print("Olá! Seja bem vindo ao chatbotLeco\n Digite x se quiser sair do Bot!\n")

nome = input("Qual o seu nome? ")

texto_selecao = '''
Digite 1 se quiser ver um pdf
Digite 2 se quiser ver o assunto sobre video do yt
Digite 3 se quiser ver o assunto de algum site
'''

while True:
    escolha_selecao = input(texto_selecao)
    if escolha_selecao == '1':
        documento = carrega_pdf()
        break
    if escolha_selecao == '2':
        documento = carrega_youtube()
        break
    elif escolha_selecao == '3':
        documento = carrega_sites()
        break
    print("Digite o valor entre 1 e 4 para cointinuar")


mensagens = []
while True:
    pergunta  = input("Usuário:")
    if pergunta.lower() == 'x':
        break
    resposta = respostas_bot(mensagens, documento)
    mensagens.append({pergunta, resposta})
    print(f'Bot: {resposta}')

print(f'Obrigado {nome} por ter usado o ChatBotLeco tenha um bom dia!')
print(f'Esse foi o nosso histórico de mensagens {mensagens}')
