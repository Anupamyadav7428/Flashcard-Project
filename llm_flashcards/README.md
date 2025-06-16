# Flashcard-Project
this is flashcard project which generate text after providing text as input text and pdf.
# AI Flashcard Generator with Ollama 🦙✨

[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-blueviolet)](https://ollama.ai/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

Transform study materials into interactive flashcards using **local LLMs via Ollama** - no API keys required!

![Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDF0dWZqY2R2b2R5d2VjZ3B5ZzB6Y2VlZ3JjbjBqZzN1ZzBqZzN1ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT5LMHxhOfscxPfIfm/giphy.gif) *(Example GIF placeholder)*

## Features 🚀

- 🦙 **100% Local AI**: Uses Ollama-hosted models (e.g., Llama3, Mistral)
- 📝 **Text/PDF Processing**: Extract content from multiple formats
- 🎓 **Customizable Prompts**: Tailor flashcard generation to your needs
- 🔄 **Real-time Preview**: See flashcards as they generate
- 📱 **Offline Capable**: Works without internet after setup

## Prerequisites 📋

1. Install [Ollama](https://ollama.ai/)
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh

2.Pull your preferred model:
ollama pull llama3  # or mistral, gemma, etc.

Installation
    git clone https://github.com/yourusername/ollama-flashcards.git
    cd ollama-flashcards
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # venv\Scripts\activate  # Windows

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver


Usage Guide
    1.Start Ollama (in separate terminal):
        ollama serve
    2.Access the app at http://localhost:8000

    3.Enter text or upload files

    4.Select model preferences:
        # In settings.py
        OLLAMA_MODEL = "llama3"  # Default model
        OLLAMA_BASE_URL = "http://localhost:11434"

Custom Prompts
    Edit utils.py to modify the flashcard generation:
    def generate_flashcards(text, subject):
        prompt = f"""
        [INST] Generate 5 concise flashcards about {subject}.
        Format strictly as:
        Q: Your question
        A: Your answer

        Text: {text[:2000]}... [/INST]
        """

        response = requests.post(
            f"{settings.OLLAMA_BASE_URL}/api/generate",
            json={
                "model": settings.OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]

Supported Models
    Model	Command	Best For
    Llama3	ollama pull llama3	General knowledge
    Mistral	ollama pull mistral	Concise answers
    Gemma	ollama pull gemma	Fast generation

Troubleshooting 
    Issue	                Solution
    "Model not found"	    Run ollama pull MODEL_NAME
    Slow responses	Try     smaller models like tinyllama
    Connection errors	    Verify Ollama is running (ollama serve)

Roadmap
    Add model temperature controls

    Implement batch processing

    Support image-based flashcards (OCR)

    Add Anki export functionality