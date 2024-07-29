from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Solution

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['solution_code', 'language']
        widgets = {
            'solution_code': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }

    def __init__(self, *args, **kwargs):
        super(SolutionForm, self).__init__(*args, **kwargs)
        self.fields['language'].choices = [('python3', 'Python 3'), ('javascript', 'JavaScript')]
        