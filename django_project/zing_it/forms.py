from django import forms
from django.contrib.auth.models import User

class Signup(forms.Form):
    full_name = forms.CharField(required=True,max_length=70)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True,min_length=5)
    confirm_password = forms.CharField(widget=forms.PasswordInput,required=True,min_length=5)




class Login(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True,min_length=5)