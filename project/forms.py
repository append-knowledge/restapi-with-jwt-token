from project.models import MyUser
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=MyUser
        fields=['username','email','password1','password2','address']

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'})
        }


class SignInform(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class UserprofileForm(ModelForm):
    class Meta:
        model=MyUser
        fields=['username','email','address']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'})
        }