import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from bs4 import BeautifulSoup

api_key = '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'
os.environ ['GROQ_API_KEY'] = api_key # variável de ambiente
chat = ChatGroq(model = 'llama-3.3-70b-versatile') #inicializando o chatbot com o modelo llama3(fornecido pela Groq)

url = 'arquivos/curriculo.pdf'
loader = PyPDFLoader(url)
lista_documentos = loader.load()

documento = ''
for doc in lista_documentos:
    documento += doc.page_content #somando o meu documento(vazio) com a lista de documentos que vai ser carregdo do youtube
#Unificando os dados em uma string


template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente simpático que tem acesso a seguintes informações: {informacoes}'),
    ('user', '{input}')
])

chain_pdf = template | chat
resposta = chain_pdf.invoke({'informacoes': documento, 'input':'Se você fosse um entrevistador de uma empresa de software, você me contrataria? Pq?'})
print(resposta.content)