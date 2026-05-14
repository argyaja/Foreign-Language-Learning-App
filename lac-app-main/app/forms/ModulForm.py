from django import forms
from app.models.Modul import Modul

class ModulForm(forms.ModelForm):
    class Meta:
        model = Modul
        fields = ['name', 'description']