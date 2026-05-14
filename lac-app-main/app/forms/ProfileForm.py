from django import forms
from app.models.Profile import Profile
from app.models.Profile import Language

class ProfileForm(forms.ModelForm):
    language = forms.ModelChoiceField(queryset=Language.objects.all(), required=False)
    
    class Meta:
        model = Profile
        fields = ['profile_picture', 'first_name', 'last_name', 'email', 'phone', 'about', 'language']

    profile_picture = forms.ImageField(required=False)