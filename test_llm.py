from agent.llm_config import get_llm

llm = get_llm()
print("LLM loaded:", type(llm))