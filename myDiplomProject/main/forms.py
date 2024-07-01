from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
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
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Password1', 'name': 'pass'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Password 2'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
