from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .services.agent_service import agent_executor

app = FastAPI(title="AI Help Bot Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatQuery(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"status": "AI Help Bot backend is running"}

@app.post("/chat")
async def handle_chat(query: ChatQuery):
    try:
        response = agent_executor.invoke({"input": query.message})
        reply = response.get("output", "Sorry, I couldn't find an output.")
        return {"reply": reply}
    except Exception as e:
        print(f"Error during agent execution: {e}")
        return {"reply": "An error occurred while processing your request."}