from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'input-field'
    }))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'input-field'
    }))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'input-field'
    }))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'input-field'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
