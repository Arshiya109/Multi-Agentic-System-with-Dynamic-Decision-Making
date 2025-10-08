# Multi-Agentic System with Dynamic Decision Making

## Overview
This system enables question answering by leveraging multiple specialized agents:
- Extracts and processes PDF documents
- Performs web searches for real-time info
- Retrieves relevant academic papers from ArXiv

The system dynamically decides which agents to invoke based on user queries, providing accurate and relevant responses.

---

## Features
- Modular architecture with clear separation of concerns
- Supports uploading PDFs and asking questions
- Integrates with external APIs like SerpAPI and ArXiv
- Safe handling of user data with privacy considerations
- Extensible for additional agents and functionalities

---

## Getting Started

### Prerequisites
- Python 3.8+
- API keys for:
     - SerpAPI (for web search)
     - Other dependencies listed in `requirements.txt`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables:
   - Create a `.env` file or set environment variables for:
     - `SERPAPI_API_KEY`
     - Any other necessary configs

### Running the Application
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## Usage
- Upload PDFs via the API or UI (if provided)
- Send questions through the API endpoint:
  
```json
{
  "question": "What is the main conclusion of the uploaded PDF?",
  "pdf_ids": ["sample1.pdf"]
}
```

- The system will process and return the answer, invoking relevant agents as needed.

---

## Architecture Highlights
- **Main API (`main.py`)**: Entry point handling user requests
- **Controller (`agents/controller.py`)**: Decides which agents to invoke
- **Agents**:
    - PDF RAG Agent
    - Web Search Agent
    - ArXiv Agent
- **Utilities** for text processing and logging

---

## Safety & Privacy
- User data is processed securely
- Files are temporarily stored and deleted after processing
- External API data transmissions are handled securely
- Content filtering applied to responses

---

## Limitations
- PDF extraction may be imperfect
- Response times depend on external API latency
- Limited context handling
- Not production hardened; further improvements needed for deployment
