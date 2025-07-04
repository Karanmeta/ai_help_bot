from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .services.agent_service import agent_executor

app = FastAPI()

# --- CORS Configuration ---
# This is the crucial part. It allows your React frontend (running on localhost:3000)
# to make API calls to your FastAPI backend (running on localhost:8000).

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- End of CORS Configuration ---


class Query(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.post("/chat")
def chat(query: Query):
    try:
        response = agent_executor.invoke({"query": query.text})
        return {"response": response.get("result", "Sorry, I could not find an answer.")}
    except Exception as e:
        print(f"Error during agent execution: {e}")
        return {"response": f"An error occurred: {e}"}
