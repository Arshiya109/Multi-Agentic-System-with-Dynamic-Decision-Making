import fitz # PyMuPDF 
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

class PDFRAGAgent:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)  # dimension depends on embedding model
        self.documents = []  # store texts
    
    def process_pdf(self, pdf_path):
        # Extract text
        doc_texts = self.extract_text_from_pdf(pdf_path)
        # Chunk and embed
        embeddings = []
        for text in doc_texts:
            embed = self.model.encode(text)
            embeddings.append(embed)
        # Build FAISS index
        self.index.add(np.array(embeddings))
        # Store documents
        self.documents.extend(doc_texts)
        # Returns the summary or first chunk as a demo
        return "PDF processed with {} chunks.".format(len(doc_texts))
    
    def extract_text_from_pdf(self, path):
        doc = fitz.open(path)
        texts = []
        for page in doc:
            texts.append(page.get_text())
        # Chunking strategy can be improved
        return texts
