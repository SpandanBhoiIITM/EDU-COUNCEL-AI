from fastapi import FastAPI
from pydantic import BaseModel
from gpt4all import GPT4All
import os

app = FastAPI()

# Path to your local model
MODEL_NAME = "ggml-gpt4all-j-v1.3-groovy"
MODEL_PATH = f"C:\\Users\\spand\\Desktop\\EDU COUNCEL AI\\{MODEL_NAME}.bin"

# Check if model file exists
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")

# Load the model
model = GPT4All(model_name=MODEL_NAME, model_path=MODEL_PATH)

class StudentInfo(BaseModel):
    name: str
    age: int
    class_level: str
    interests: list[str]
    dislike: list[str]

@app.post("/counsel")
async def get_counsel(data: StudentInfo):
    prompt = (
        f"My name is {data.name}, I am {data.age} years old and currently studying in {data.class_level}.\n"
        f"My favorite subjects are: {', '.join(data.interests)}.\n"
        f"I dislike: {', '.join(data.dislike)}.\n"
        "Based on this, suggest a suitable stream (Science, Commerce, or Arts) for my future studies. "
        "Explain your reasoning in simple, student-friendly language."
    )

    with model.chat_session():
        output = model.generate(prompt, max_tokens=300, temp=0.7)

    return {"response": output}
