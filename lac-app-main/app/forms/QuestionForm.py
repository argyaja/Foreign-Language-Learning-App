# from django import forms
# from app.models.Question import Question

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ['name', 'email', 'query']



from django import forms
from app.models.Question import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'email', 'query']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'query': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Post Your Query'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Nama tidak boleh mengandung angka atau karakter lain")
        return name

    def clean_query(self):
        query = self.cleaned_data.get('query')
        if len(query) < 10:
            raise forms.ValidationError("Pertanyaan minimal memiliki panjang 10 karakter")
        return query

