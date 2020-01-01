from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Userinfo(forms.ModelForm):
   
    class Meta:
        model = User
        fields = ["username","password","email"]

        error_messages = {
            'username':{
                'unique':"the username or password is incorrect",
            }
           
        }       
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'user','id':'',"placeholder":"Username"}),
            'password': forms.PasswordInput(attrs={'class': 'pass','id':'',"placeholder":"Password"}),
            'email': forms.EmailInput(attrs={'class': 'user','id':'',"placeholder":"Email"}),

        }

