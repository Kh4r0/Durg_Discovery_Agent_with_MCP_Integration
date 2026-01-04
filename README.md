🧬 Drug Discovery AI Agent with LangChain + MCP + FastAPI
An AI-powered Drug Discovery Agent that accepts a drug name or natural language query, performs LLM-based reasoning, integrates MCP (Model Context Protocol) tools for fact-checking and safety analysis, and returns validated drug recommendations through a FastAPI API.

🚀 Key Features
🔬 Drug analysis using natural language queries
🧠 LangChain-based agent reasoning
🔗 MCP integration for scientific fact checking
⚠️ Drug safety & side-effect recommendations
🌐 FastAPI REST API
📄 Structured outputs using Pydantic schemas

🛠️ Tech Stack
Python
LangChain
FastAPI
Pydantic
Groq LLM
MCP (Model Context Protocol)
dotenv
Git & GitHub

📂 Project Structure
DRUG_AGENT/
│
├── .venv/                         # Python virtual environment
│   └── pyvenv.cfg
│
├── agent/                         # Core agent logic
│   ├── __init__.py
│   ├── llm_config.py              # LLM & API key configuration
│   ├── main_agent.py              # Main agent orchestration logic
│   ├── prompts.py                 # System and agent prompts
│   ├── schemas.py                 # Pydantic response schemas
│   └── __pycache__/
│
├── mcp/                           # MCP tools
│   ├── __init__.py
│   ├── drug_fact_checker.py       # Drug fact validation module
│   ├── safety_recommender.py      # Drug safety & recommendation logic
│   └── __pycache__/
│
├── api_server.py                  # FastAPI application entry point
├── requirements.txt               # Project dependencies
├── README.md                      # Project documentation
│
├── test_groq.py                   # Groq API test
├── test_import.py                 # Import validation test
├── test_key.py                    # API key test
├── test_llm.py                    # LLM response test
│
└── .env                           # Environment variables

🧠 How the Agent Works (Flow)
User Input
Accepts drug name or natural language query
Example: “Is Paracetamol safe for long-term use?”
Agent Reasoning (LangChain)
Query is interpreted by the LLM
Agent determines required actions

MCP Tool Execution
drug_fact_checker.py validates scientific claims
safety_recommender.py analyzes risks and usage guidelines
Response Structuring
Output is formatted using Pydantic schemas

API Response
Final validated response returned via FastAPI

🌐 API Endpoints
🔹 Health Check
GET /
Response
{
  "status": "Drug Discovery Agent API is running"
}
🔹 Ask the Drug Agent
POST /ask
Request

Json
{
  "question": "What are the side effects of Aspirin?"
}
Response

Json
{
  "query": "What are the side effects of Aspirin?",
  "analysis": "Aspirin may cause gastrointestinal irritation...",
  "fact_check": "Verified using MCP drug fact checker",
  "recommendations": [
    "Avoid prolonged use without medical advice",
    "Not recommended for children with viral infections"
  ]
}

⚙️ Setup & Run Instructions

git clone https://github.com/your-username/drug-agent.git
cd DRUG_AGENT
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn api_server:app --reload

🧪 Testing
test_groq.py → Tests Groq LLM connection
test_key.py → Verifies API keys
test_llm.py → Confirms LLM responses
test_import.py → Validates imports