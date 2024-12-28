api_key = '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'

import os #biblioteca do sistema operacional

os.environ ['GROQ_API_KEY'] = api_key # variável de ambiente

from langchain_groq import ChatGroq #biblioteca da Groq
#Langchain puxa outras bibliotecas menores

chat = ChatGroq(model = 'llama-3.3-70b-versatile') #inicializando o chatbot com o modelo Ilhama3(fornecido pela Groq)