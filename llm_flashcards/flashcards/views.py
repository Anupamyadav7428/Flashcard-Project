
from django.shortcuts import render
from .forms import FlashcardForm
from .utils import extract_text_from_pdf, generate_flashcards


def index(request):
    flashcards = None
    if request.method == "POST":
        form = FlashcardForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            text_input = form.cleaned_data['input_text']
            file = form.cleaned_data['upload_file']

            text = text_input
            if file:
                if file.name.endswith('.pdf'):
                    text = extract_text_from_pdf(file)
                elif file.name.endswith('.txt'):
                    text = file.read().decode("utf-8")

            if text:
                flashcards_raw = generate_flashcards(text, subject)
                # Split the flashcards by newline and filter out empty lines
                flashcards = [card.strip() for card in flashcards_raw.split('\n') if card.strip()]
    else:
        form = FlashcardForm()
    return render(request, 'index.html', {'form': form, 'flashcards': flashcards})
