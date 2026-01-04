# agent/prompts.py
from langchain.prompts import ChatPromptTemplate

AGENT_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "You are an AGI-level scientific drug discovery assistant. "
     "Use verified scientific reasoning. Do NOT hallucinate."),
    ("human", "{query}")
])
