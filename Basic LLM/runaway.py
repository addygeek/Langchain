import os
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI(temperature=0)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "I am going to Europe, what should I pack?"

print(llm_chain.run(question))