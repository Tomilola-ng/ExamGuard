from django import forms
from .models import Answer

# Create your tests here.
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']