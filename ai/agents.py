from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List

class AgentState(TypedDict):
    query: str
    context: List[str]
    response: str

def retrieve_documents(state: AgentState):
    # Logic to fetch from Qdrant/VectorDB
    return {"context": ["Document snippet 1", "Document snippet 2"]}

def generate_answer(state: AgentState):
    # Logic to call LLM with context
    return {"response": "This is the AI generated answer based on context."}

workflow = StateGraph(AgentState)
workflow.add_node("retrieve", retrieve_documents)
workflow.add_node("generate", generate_answer)

workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

app = workflow.compile()
