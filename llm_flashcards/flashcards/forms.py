from django import forms

class FlashcardForm(forms.Form):
    subject = forms.CharField(required=False)
    input_text = forms.CharField(widget=forms.Textarea, required=False)
    upload_file = forms.FileField(required=False)
