from django import forms
from .models import Miasto

class MiastoForm(forms.ModelForm):
    class Meta:
        model = Miasto
        fields = ['nazwa']
        labels = {'nazwa': ''}