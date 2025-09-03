# 🎓 EDU-COUNSEL-AI:

An AI-powered FastAPI application that recommends academic streams and subject choices for classes 10, 11, and 12 based on student preferences and dislikes, helping plan future studies effectively.
🌟 Features

Personalized Academic Recommendations: AI analyzes student preferences to suggest suitable academic streams
Stream Selection: Recommends between Science, Commerce, or Arts streams
Student-Friendly Explanations: Provides reasoning in simple, easy-to-understand language
FastAPI Backend: High-performance API with automatic documentation
Flexible AI Integration: Support for both cloud-based (Gemini) and local (GPT4All) AI models

🚀 Getting Started
Prerequisites
bashPython 3.8+
FastAPI
GPT4All (for local model) OR Gemini API access
Installation

Clone the repository:

bashgit clone the repo
cd EDU-COUNSEL-AI

Install dependencies:

bashpip install -r requirements.txt

Set up environment variables (for Gemini API version):

bash# Create .env file
GEMINI_API_KEY=your_api_key_here

For local model setup:

Download GPT4All model: ggml-gpt4all-j-v1.3-groovy.bin
Place it in your project directory
Update the MODEL_PATH in main.py


Run the application:

bash# For cloud-based version
uvicorn app:app --reload

# For local model version  
uvicorn main:app --reload

Access the API documentation:

Open your browser and go to http://127.0.0.1:8000/docs



🏗️ System Architecture
Student Input → FastAPI → AI Model (Gemini/GPT4All) → Stream Recommendation → Response
Core Components

FastAPI Application: High-performance web framework for the API
AI Integration:

Cloud Option: Gemini API integration (app.py)
Local Option: GPT4All local model (main.py)


Data Models: Pydantic models for request/response validation
Recommendation Engine: AI-powered academic counseling logic

🤖 AI Models
Cloud-Based Version (app.py)

Model: Gemini API
Advantages: Always up-to-date, no local storage required
Requirements: Internet connection, API key

Local Version (main.py)

Model: GPT4All (ggml-gpt4all-j-v1.3-groovy)
Advantages: Privacy-focused, no internet required, no API costs
Requirements: Local model file (~4GB)

📊 API Usage
Endpoint: POST /counsel
Request Body:
json{
    "name": "John Doe",
    "age": 16,
    "class_level": "Class 10",
    "interests": ["Mathematics", "Physics", "Computer Science"],
    "dislike": ["History", "Literature"]
}
Response:
json{
    "response": "Based on your strong interest in Mathematics, Physics, and Computer Science, I recommend the Science stream for your future studies. Your logical thinking and problem-solving skills in these subjects indicate you'd excel in scientific fields..."
}
Python Client Example
pythonimport requests
import json

url = "http://127.0.0.1:8000/counsel"

student_data = {
    "name": "Alice Smith",
    "age": 15,
    "class_level": "Class 10",
    "interests": ["Business Studies", "Economics", "Mathematics"],
    "dislike": ["Biology", "Chemistry"]
}

response = requests.post(url, json=student_data)
recommendation = response.json()

print(recommendation["response"])
📁 Project Structure
EDU-COUNSEL-AI/
├── app.py                     # Cloud-based FastAPI app (Gemini)
├── main.py                    # Local FastAPI app (GPT4All)
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (for API keys)
├── tempCodeRunnerFile.py      # Temporary file
├── LICENSE                    # MIT License
├── README.md                  # Project documentation

🎯 Academic Streams Covered
Science Stream

Subjects: Physics, Chemistry, Mathematics, Biology
Career Paths: Engineering, Medicine, Research, Technology
Suitable for: Students interested in STEM fields

Commerce Stream

Subjects: Accountancy, Business Studies, Economics
Career Paths: Business, Finance, CA, CS, Management
Suitable for: Students interested in business and finance

Arts/Humanities Stream

Subjects: History, Geography, Psychology, Literature
Career Paths: Law, Journalism, Social Work, Civil Services
Suitable for: Students interested in social sciences and humanities

🔧 Configuration
Environment Variables (.env)
bash# For Gemini API version
GEMINI_API_KEY=your_gemini_api_key_here

# Optional: Custom API URL
GEMINI_API_URL=https://api.gemini.example.com/v1/chat/completions
Model Configuration (main.py)
python# Local model settings
MODEL_NAME = "ggml-gpt4all-j-v1.3-groovy"
MODEL_PATH = "C:\\path\\to\\your\\model\\{MODEL_NAME}.bin"

# Generation parameters
MAX_TOKENS = 300
TEMPERATURE = 0.7
🧪 Testing the API
Using curl:
bashcurl -X POST "http://127.0.0.1:8000/counsel" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Test Student",
       "age": 16,
       "class_level": "Class 10",
       "interests": ["Mathematics", "Physics"],
       "dislike": ["History"]
     }'
Using FastAPI's interactive docs:

Start the server: uvicorn app:app --reload
Go to: http://127.0.0.1:8000/docs
Try out the /counsel endpoint directly in the browser

🚀 Deployment Options
Local Development
bashuvicorn app:app --reload --host 0.0.0.0 --port 8000
Production Deployment
bashuvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
Docker Deployment
dockerfileFROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
📈 Performance Considerations

Cloud Model (Gemini):

Response time: ~2-5 seconds
Dependent on internet speed and API response time


Local Model (GPT4All):

Response time: ~10-30 seconds (depending on hardware)
No internet required
Model loading time: ~5-10 seconds on startup



🔒 Security & Privacy

Local Model: Complete privacy, all processing done locally
Cloud Model: Data sent to external API (review provider's privacy policy)
No Data Storage: Application doesn't store student information
Input Validation: Pydantic models ensure data integrity

🤝 Contributing

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📋 Requirements
txtfastapi
uvicorn
pydantic
httpx
python-dotenv
gpt4all
🐛 Troubleshooting
Common Issues:

Model file not found:

Ensure the GPT4All model is downloaded and path is correct
Check file permissions


API key issues:

Verify your Gemini API key is valid
Check the .env file is properly configured


Port already in use:

Change the port: uvicorn app:app --port 8001



📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

GPT4All for providing local AI model capabilities
FastAPI for the excellent web framework
Gemini API for cloud-based AI integration
Educational institutions for guidance on academic streams

📞 Contact
SpandanBhoiITM - GitHub Profile
Project Link: https://github.com/SpandanBhoiIITM/

⭐ Star this repository if it helps students make better academic choices! ⭐
