from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from .models import Article, Grade, Comment, Support


class ArticleModelForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class GradeModelForm(ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'


class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'email']


class SupportModelForm(ModelForm):
    class Meta:
        model = Support
        fields = '__all__'


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password1'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password2'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password' }))
