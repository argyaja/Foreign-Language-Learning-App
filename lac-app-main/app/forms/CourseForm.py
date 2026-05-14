from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from app.models.Course import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'image', 'description', 'flag_icon']
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and hasattr(image, 'content_type'):
            if not image.content_type in ['image/jpeg', 'image/png']:
                raise forms.ValidationError('Please select a JPG or PNG file.')
        return image
