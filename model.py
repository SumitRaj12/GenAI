import os
from dotenv import load_dotenv
from langchain.llms import Cohere
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load environment variables from .env file
load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
# Fetch the Cohere API key from environment variables
cohere_api_key = os.getenv('COHERE_API_KEY')

# Initialize the Cohere LLM through LangChain
cohere_llm = Cohere(cohere_api_key=cohere_api_key)

# Set up conversation memory to hold the context
memory = ConversationBufferMemory()

# Create a conversation chain with the LLM and memory
conversation = ConversationChain(llm=cohere_llm, memory=memory)

# Example conversation
user_input = "Hello, who are you?"
response = conversation.predict(input=user_input)
print(f"User: {user_input}")
print(f"AI: {response}")