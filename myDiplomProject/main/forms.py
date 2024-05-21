from django.forms import ModelForm, forms
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
        fields = '__all__'


class SupportModelForm(ModelForm):
    class Meta:
        model = Support
        fields = '__all__'


class RegisterForm(UserCreationForm):
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
