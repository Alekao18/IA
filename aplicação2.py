#import os #biblioteca do sistema operacional
#from langchain_groq import ChatGroq #biblioteca da Groq
from langchain_community.document_loaders import WebBaseLoader #ferramenta dentro da langchain onde acessa documentos carregador da internet
#from langchain.prompts import ChatPromptTemplate

#api_key = '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'
#os.environ ['GROQ_API_KEY'] = api_key # variável de ambiente

loader = WebBaseLoader('https://asimov.academy/')
lista_documentos = loader.load()
print(lista_documentos)
#chat = ChatGroq(model = 'llama-3.3-70b-versatile') #inicializando o chatbot com o modelo llama3(fornecido pela Groq)