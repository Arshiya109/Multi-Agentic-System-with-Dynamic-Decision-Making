from transformers import pipeline

class ControllerAgent:
    def __init__(self):
        # Initialize LLM or rule-based decision system
        # For demo, using simple rule-based logic
        self.llm = pipeline("text-generation", model="gpt2")  
    
    def decide(self, query: str):
        agents = []
        reasoning = ""
        pdf_path = None

        # Simple rules
        if "summarize" in query.lower():
            # Assume PDF uploaded and relevant
            agents.append('pdf')
            reasoning = "Query asks for summarization; calling PDF RAG agent."
        elif "arxiv" in query.lower() or "recent papers" in query.lower():
            agents.append('arxiv')
            reasoning = "Query mentions arxiv or recent papers; calling ArXiv agent."
        elif "news" in query.lower() or "latest" in query.lower():
            agents.append('web')
            reasoning = "Query asks for news or latest info; calling Web Search agent."
        else:
            # Default to web search
            agents.append('web')
            reasoning = "Default routing to Web Search."
        
        return {
            "agents": agents,
            "reasoning": reasoning,
            "pdf_path": pdf_path
        }
