import argparse
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
import json
import os
import requests

# example JSON object:
# {
#     "template": "You are a friendly chatbot assistant that responds conversationally to users' questions. \n Keep the answers short, unless specifically asked by the user to elaborate on something. \n \n Question: {question} \n \n Answer:",
#     "parameters": {"question": "What is a chatbot?"}
# }

os.environ["HF_DATASETS_OFFLINE"]="1" 
os.environ["TRANSFORMERS_OFFLINE"]="1"

parser = argparse.ArgumentParser(description="Lilypad LLM")
parser.add_argument("--i", dest="ipfs", type=str, help="IPFS Hash", required=True)

args=parser.parse_args()
ipfs=args.ipfs

model_id = "lmsys/fastchat-t5-3b-v1.0"
llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text2text-generation",
    model_kwargs={"temperature": 0, "max_length": 1000},
    # device=0
)

default_template = """
You are a friendly chatbot assistant that responds conversationally to users' questions.
Keep the answers short, unless specifically asked by the user to elaborate on something.

Question: {question}

Answer:"""


r = requests.get(f"https://ipfs.io/ipfs/{ipfs}/")
content  = r.content

print(content)

json_content = json.loads(content)

print(json_content)

prompt = PromptTemplate.from_template(json_content["template"])
for key in prompt.input_variables:
    if key not in json_content["parameters"]:
        json_content["parameters"][key]=""

llm_chain = LLMChain(prompt=prompt, llm=llm)

result = llm_chain(json_content["parameters"])

print(result)

f = open("./outputs/result.json", "w")
json.dump(result, f)
f.close()
