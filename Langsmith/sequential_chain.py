from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ['LANGCHAIN_PROJECT'] = 'sequential_chain_example'

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model1 = ChatOpenAI(api_key=os.getenv("api_key"), temperature=0.7,model="gpt-4o-mini")

model2 = ChatOpenAI(api_key=os.getenv("api_key"), temperature=0.5,model="gpt-4o")

parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model2 | parser

config={
    'run_name': 'Sequential Chain for Report Generation',
    'tags': ['sequential_chain', 'report_generation','summarization'],
    'metadata': {'model1': 'gpt-4o-mini', 'model1_temp':'0.7','model2': 'gpt-4o','model2_temp':'0.5','parser':'StrOutputParser'}
}

result = chain.invoke({'topic': 'Unemployment in India'},config=config)

print(result)


