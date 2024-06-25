# from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from environment variables
cohere_api_key = os.getenv('COHERE_API_KEY')
# llm = OpenAI(openai_api_key=Openai_api_key)

# response = llm.invoke("List the seven wonders of the world.")
# print(response)
import cohere

co = cohere.Client(cohere_api_key)
fact = 'hillary responds to creepy joe biden caught groping dozens of young women also michelle obama hosts an event for rappers who promote rape alex jones  infowarscom  october   comments  as if the potus race could not get any creepier  we now have mr groping young girls vp joe biden come out against the words donald trump used  alex jones illustrates how biden hillary and tim kaine are some of the creepiest people around newsletter sign up get the latest breaking news  specials from alex jones and the infowars crew related articles download on your mobile device now for free today on the show get the latest breaking news  specials from alex jones and the infowars crew from the store featured videos featured videos a vote for hillary is a vote for world war   see the rest on the alex jones youtube channel  the most offensive halloween ever  see the rest on the alex jones youtube channel  illustration how much will your healthcare premiums rise in     infowarscom is a free speech systems llc company all rights reserved digital millennium copyright act notice   flip the switch and supercharge your state of mind with brain force the next generation of neural activation from infowars life '
response = co.chat(
	message=f"predict whether it is true or fake {fact} and provide the percentage of confidence"
)

print(response.text)
