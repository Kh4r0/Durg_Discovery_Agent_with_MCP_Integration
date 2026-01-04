from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# Import Agent Orchestration
# --------------------------------------------------
from agent.main_agent import run_agent
from agent.schemas import AgentResponse

# --------------------------------------------------
# FastAPI App
# --------------------------------------------------
app = FastAPI(
    title="Drug Discovery Agent API",
    description="AGI-style scientific drug discovery agent with MCP-based fact checking and recommendations",
    version="2.0.0"
)

# --------------------------------------------------
# Request Schema
# --------------------------------------------------
class QueryRequest(BaseModel):
    question: str

# --------------------------------------------------
# Health Check
# --------------------------------------------------
@app.get("/")
def health_check():
    return {
        "status": "running",
        "agent": "Drug Discovery AGI Agent",
        "version": "2.0.0"
    }

# --------------------------------------------------
# Main Agent Endpoint
# --------------------------------------------------
@app.post("/ask", response_model=AgentResponse)
def ask_agent(request: QueryRequest):
    try:
        # Call AGI Agent (LangChain + MCP)
        result = run_agent(request.question)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Agent execution failed: {str(e)}"
        )
