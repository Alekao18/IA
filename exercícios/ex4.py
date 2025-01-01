api_key = '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'

import os #biblioteca do sistema operacional

os.environ ['GROQ_API_KEY'] = api_key # variável de ambiente

from langchain_groq import ChatGroq #biblioteca da Groq
#Langchain puxa outras bibliotecas menores

chat = ChatGroq(model = 'llama-3.3-70b-versatile') #inicializando o chatbot com o modelo llama3(fornecido pela Groq)
#llama3 é um modelo de linguagem grande e gratuito da META

pergunta = input('Usuario: ')
resposta = chat.invoke(pergunta)
print(resposta.content)#mostra a resposta do chatbot invocado
#.content, mostra apenas o conteúdo do que a gente pediu(reposta)
#ll3(llama3) um modelo de IA programada com diversos parâmetros , como a capacidade de aprender, raciocinar e etc. Pronta para acessarmos e utilizarmos!