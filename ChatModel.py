from langchain_cohere import ChatCohere
from langchain.schema.messages import HumanMessage, SystemMessage

import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')

co = ChatCohere(cohere_api_key=COHERE_API_KEY)

message = [
     SystemMessage(content="You are Rahul Gandhi."),
    HumanMessage(content="Which shoe manufacturer are you associated with?"),
]
res = co.invoke(message)
print(res.content)
