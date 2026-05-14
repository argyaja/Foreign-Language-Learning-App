
from django import forms
from app.models.UserDetails import UserDetails

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['first_name', 'last_name', 'email', 'phone', 'about', 'profile_picture']


