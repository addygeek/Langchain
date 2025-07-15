from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()


hf_api_token = os.getenv("HUGGINGFACE_API_TOKEN")

# Specify the model repo (e.g., 'meta-llama/Llama-2-7b-chat-hf')
repo_id = "meta-llama/Llama-2-7b-chat-hf"

llm = HuggingFaceHub(
    repo_id=repo_id,
    huggingfacehub_api_token=hf_api_token
)

prompt = PromptTemplate(
    input_variables=["question"],
    template="Q: {question}\nA:"
)

chain = LLMChain(llm=llm, prompt=prompt)

question = "What is LangChain?"
response = chain.run(question=question)
print(response)