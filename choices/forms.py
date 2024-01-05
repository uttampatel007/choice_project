from django import forms
from .models import Choice


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text', 'choice_description', 'date')


