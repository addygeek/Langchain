import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


os.environ["OPENAI_API_KEY"]

llm = OpenAI(temperature=0.7)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="What are 5 interesting facts about {topic}?",
)

chain = LLMChain(llm=llm, prompt=prompt)

topic = "the moon"
response = chain.run(topic)

print(response)