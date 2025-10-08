from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
import uuid
import os
from agents.controller import ControllerAgent
from agents.pdf_rag import PDFRAGAgent
from agents.web_search import WebSearchAgent
from agents.arxiv_agent import ArxivAgent

app = FastAPI()

# Initialize agents
controller = ControllerAgent()
pdf_agent = PDFRAGAgent()
web_agent = WebSearchAgent()
arxiv_agent = ArxivAgent()

# Storage for uploaded PDFs
UPLOAD_DIR = "uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# In-memory logs 
logs = []

class AskRequest(BaseModel):
    query: str

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    filename = f"{uuid.uuid4()}.pdf"
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())
    # Store metadata if needed
    return {"message": "PDF uploaded", "file_path": filepath}

@app.post("/ask/")
async def ask_question(request: AskRequest):
    query = request.query
    # Controller decides which agents to call
    decision_trace = controller.decide(query)
    # Based on decision, call agents
    responses = {}
    used_agents = decision_trace['agents']
    rationale = decision_trace['reasoning']
    
    if 'pdf' in used_agents:
        pdf_response = pdf_agent.process_pdf(decision_trace.get('pdf_path'))
        responses['PDF Summary'] = pdf_response
    if 'web' in used_agents:
        web_response = web_agent.search(query)
        responses['Web Search'] = web_response
    if 'arxiv' in used_agents:
        arxiv_response = arxiv_agent.search(query)
        responses['ArXiv'] = arxiv_response
    
    # Synthesize final answer using LLM (placeholder)
    final_answer = "Combined answer based on agents' responses."
    
    # Log the interaction
    logs.append({
        "query": query,
        "decision": decision_trace,
        "responses": responses,
        "final_answer": final_answer,
        "timestamp": str(uuid.uuid1())
    })
    
    return {
        "answer": final_answer,
        "agents_used": used_agents,
        "rationale": rationale,
        "responses": responses
    }

@app.get("/logs/")
def get_logs():
    return logs
