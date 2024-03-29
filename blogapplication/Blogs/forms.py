from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post
class Postform(forms.ModelForm):
    class Meta:
        model=Post;
        fields=['title','author','desc'];
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),'author':forms.TextInput(attrs={'class':'form-control'}),'desc':forms.Textarea(attrs={'class':'form-control'}),}
class BlogForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':"EMAIL"}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
