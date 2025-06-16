import PyPDF2
import requests
import subprocess
from django.conf import settings

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return " ".join(page.extract_text() for page in reader.pages if page.extract_text())




def generate_flashcards(text, subject):
    try:
        # Optimized prompt for 15 flashcards
        prompt = f"""Generate exactly 15 high-quality flashcards about {subject} using this strict format:
        Q1: [question]
        A1: [concise answer]
        Q2: [question] 
        A2: [answer]
        ...
        Q15: [question]
        A15: [answer]
        
        Reference text: {text[:1000]}"""
        
        # Try API first
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3:8b",
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "num_ctx": 2048,
                        "num_thread": 6
                    }
                },
                timeout=120
            )
            data = response.json()
            if data.get("response"):
                return data["response"]
        except requests.exceptions.RequestException:
            pass  # Fall through to CLI method
        
        # Fallback to CLI if API fails
        result = subprocess.run(
            ["ollama", "run", "llama3:8b", prompt],
            capture_output=True,
            text=True,
            timeout=180
        )
        
        if result.stdout:
            return result.stdout
        return "Failed to generate content after multiple attempts"
        
    except Exception as e:
        return f"System error: {str(e)}"

