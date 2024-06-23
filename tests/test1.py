import langgraph as l
import os
import dotenv
dotenv.load_dotenv()

api_key = os.environ['GROQ_API']

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key=api_key
)

system = "You are a helpful assistant."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat
answer = chain.invoke({"text": "who is the president of the united states?"})

print(answer)