from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.output_parsers import RegexParser
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader

# Step 1: Load documents and create a retriever
loader = TextLoader("sample_docs.txt")
docs = loader.load()
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever()

# Step 2: Define prompt templates
summary_prompt = PromptTemplate(
    input_variables=["context"],
    template="Summarize the following text:\n{context}"
)
question_prompt = PromptTemplate(
    input_variables=["summary"],
    template="Based on this summary, generate three questions:\n{summary}"
)

# Step 3: Define LLMs
llm = OpenAI(temperature=0.7)

# Step 4: Define output parser
parser = RegexParser(
    regex=r"Question \d+: (.*)",
    output_keys=["question"]
)

# Step 5: Create chains
summary_chain = LLMChain(llm=llm, prompt=summary_prompt)
question_chain = LLMChain(llm=llm, prompt=question_prompt, output_parser=parser)

# Step 6: Sequential chain
overall_chain = SequentialChain(
    chains=[summary_chain, question_chain],
    input_variables=["context"],
    output_variables=["question"]
)

# Step 7: Run the chain with retrieved context
query = "What is LangChain?"
retrieved_docs = retriever.get_relevant_documents(query)
context = " ".join([doc.page_content for doc in retrieved_docs])
result = overall_chain.run(context=context)
print(result)