from fastapi import FastAPI,Request
from pydantic import BaseModel
import requests

app=FastAPI()

HUGGINGFACE_API="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"
class studentinfo(BaseModel):
  name:str
  age:int
  class_level:str
  interests: list[str]
  dislike: list[str]
@app.get("/")
async def root():
    return {"message": "Welcome to EDU COUNSEL AI API"}

@app.post("/counsel")
def counsel(student:studentinfo):
  prompt=(
      f"My name is {student.name}, I am {student.age} years old, studying in {student.class_level}.\n"
      f"I like {', '.join(student.interests)} and dislike {', '.join(student.dislike)}.\n"
      f"Please give me personalized academic and career guidance in 3-5 lines."
  )
  response = requests.post(
      "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
      headers={"Authorization": f"Bearer {HUGGINGFACE_API}"},
      json={"inputs": prompt}
  )

  if response.status_code == 200:
      result = response.json()
      generated_text = result[0]["generated_text"]
      return {"response": generated_text}
  else:
      return {"response": f"Error from Hugging Face: {response.text}"}