import argparse
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
import json

model_id = "lmsys/fastchat-t5-3b-v1.0"
llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text2text-generation",
    model_kwargs={"temperature": 0, "max_length": 1000},
    device=1
)

default_template = """
You are a friendly chatbot assistant that responds conversationally to users' questions.
Keep the answers short, unless specifically asked by the user to elaborate on something.

Question: {question}

Answer:"""

parser = argparse.ArgumentParser(description="Lilypad LLM")
parser.add_argument("--t", dest="template", type=str, help="Langchain template", default=default_template)
parser.add_argument("--p", dest="parameters", type=str, help="Number of Images",default='{"question":"What is an AI bot"}')

args=parser.parse_args()
template=args.template
parameters=json.loads(args.parameters)

prompt = PromptTemplate.from_template(template)
for key in prompt.input_variables:
    if key not in parameters:
        parameters[key]=""

llm_chain = LLMChain(prompt=prompt, llm=llm)

result = llm_chain(parameters)

print(result)

f = open("./output/result.json", "w")
json.dump(result, f)
f.close()
