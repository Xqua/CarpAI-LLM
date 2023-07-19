# CarpAI-LLM

This is a docker image to test the implementation of an LLM on the lilypad stack. 

## Requierements

- docker
- docker compose

- hugging face key

## Usage

The script takes one argument, the CID of the ipfs JSON file to be used as input

```
usage: main.py [-h] --i IPFS

Lilypad LLM

options:
  -h, --help  show this help message and exit
  --i IPFS    IPFS Hash
  ```

### JSON Inputs
The script uses IPFS files as inputs to do inferences, The JSON files must have the following formating, which follows langchain formats:

```json
{
    "template": "You are a friendly chatbot assistant that responds conversationally to users' questions. \n Keep the answers short, unless specifically asked by the user to elaborate on something. \n \n Question: {question} \n \n Answer:",
    "parameters": {"question": "What is a chatbot?"}
}
```

### Docker

1) build the image using the docker compose stack:
 - `docker compose build` 

2) Upload the image to the docker hub
- `docker tag CID HUB/NAME:VERSION`

3) Use the image with bacalhau
- `bacalhau docker run --gpu 1 HUB/NAME:VERSION -- python main.py --i CID`

4) Use this image with lilypad
/!\ DOES NOT WORK YET /!\
- `lilypad run fastchat:v0.0.1 CID`