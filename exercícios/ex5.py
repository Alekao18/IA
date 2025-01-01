import os #biblioteca do sistema operacional
from langchain_groq import ChatGroq #biblioteca da Groq
from langchain_community.document_loaders import WebBaseLoader #ferramenta dentro da langchain onde acessa documentos carregador da internet
from langchain.prompts import ChatPromptTemplate

api_key = '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'
os.environ ['GROQ_API_KEY'] = api_key # variável de ambiente
chat = ChatGroq(model = 'llama-3.3-70b-versatile') #inicializando o chatbot com o modelo llama3(fornecido pela Groq)

loader = WebBaseLoader('https://asimov.academy/') #carregando o site do Duolingo
lista_documentos = loader.load() #fazendo scrape(leitura/analise) do site

def respostas_bot(mensagens,documento):
    mensagem_system = '''Você é um assistente amigável chamado Leco e tem acesso a seguintes informações: {documentos_informados}'''
    mensagens_modelo = [('system', mensagem_system)]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    respostas = chain.invoke({'documentos_informados': documento})
    return respostas.content

documento = ''
for doc in lista_documentos:
    documento += doc.page_content
#Unificando os dados em uma string

'''template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável chamado Leco e tem acesso a seguintes informações: {documentos_informados}'),
    ('user', '{input}') #template das mensagens
])'''

mensagens = []
while True:
    pergunta = input('USUARIO: ')
    resposta = respostas_bot(mensagens, documento)
    mensagens.append
    print(f'BOT: {resposta}')