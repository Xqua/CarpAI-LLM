from huggingface_hub import hf_hub_download
import os

HUGGING_FACE_API_KEY = os.environ("HUGGING_FACE_API_KEY")

# Replace this if you want to use a different model
model_id, filename = ("lmsys/fastchat-t5-3b-v1.0", "pytorch_model.bin") 

downloaded_model_path = hf_hub_download(
    repo_id=model_id,
    filename=filename,
    token=HUGGING_FACE_API_KEY
)

print(downloaded_model_path)
