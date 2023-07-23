from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import Profile
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='passwordni kiriting:',
                             widget=forms.PasswordInput)
    password_2=forms.CharField(label='passwordni takrorlang:',
                             widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','email']
    def clean_password_2(self):
        data=self.cleaned_data
        if data['password'] != data['password_2']:
            raise forms.ValidationError("ikkala paasword bir-biriga teng bo'lishi shart !") 
        return data['password_2']
class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['photo','data_of_birth']