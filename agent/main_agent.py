# agent/agent_core.py
from agent.llm_config import get_llm
from agent.schemas import AgentResponse
from agent.prompts import AGENT_PROMPT

from mcp.drug_fact_checker import drug_fact_checker
from mcp.safety_recommender import safety_recommendation

def run_agent(query: str) -> AgentResponse:
    llm = get_llm()

    # Step 1: Reasoning
    chain = AGENT_PROMPT | llm
    answer = chain.invoke({"query": query}).content

    # Step 2: MCP Context Injection
    facts = drug_fact_checker(query)
    recommendations = safety_recommendation(query)

    return AgentResponse(
        answer=answer,
        fact_check=facts,
        recommendations=recommendations
    )
