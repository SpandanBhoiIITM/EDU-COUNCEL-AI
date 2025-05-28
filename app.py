from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()

API_KEY = os.getenv("GEMINI_API_KEY")  
API_URL = "https://api.gemini.example.com/v1/chat/completions"  

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

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    json_data = {
        "model": "gemini-1",  
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.7
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, headers=headers, json=json_data)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"LLM API request failed: {response.text}")

        response_data = response.json()
        answer = response_data["choices"][0]["message"]["content"]
    
    return {"response": answer}
