from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Article, Grade, Comment, Language
from .forms import ArticleModelForm, RegisterForm, GradeModelForm, SupportModelForm, CommentModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django import forms

def main(request):
    return render(request, 'main.html')

def main2(request):
    return render(request, 'main2.html')


def sport(request):
    sports = Article.objects.filter(category='sport')
    return render(request, 'topic/sport.html', {'sports': sports[::-1]})


def scince(request):
    scinces = Article.objects.filter(category='scince')
    return render(request, 'topic/scince.html', {'scinces': scinces[::-1]})


def cooking(request):
    cookings = Article.objects.filter(category='cooking')
    return render(request, 'topic/cooking.html', {'cookings': cookings[::-1]})


def technic(request):
    technics = Article.objects.filter(category='technic')
    return render(request, 'topic/technic.html', {'technics': technics[::-1]})


def help(request):
    return render(request, 'help/help.html')



def support(request):
    return render(request, 'help/support.html')

def successfully(request):
    return render(request, 'help/successfully.html')
class MyDetailView(DetailView):
    model = Article
    template_name = 'detail/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentModelForm()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.get_object()
            comment.save()
            return redirect(request.path)
        return self.get(self, request, *args, **kwargs)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')

    else:
        form = ArticleModelForm()
    return render(request, 'detail/create.html', {'form': form})


def registr(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            users = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/registr.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'](forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username'}))), password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def grade_forms(request):
    if request.method == 'POST':
        form = GradeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade')

    else:
        form = GradeModelForm()
    return render(request, 'grade/grade_forms.html', {'form': form})


def grade(request):
    grades = Grade.objects.all()
    return render(request, 'grade/grade.html', {'grades': grades})


def support(request):
    if request.method == 'POST':
        form = SupportModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('successfully')

    else:
        form = SupportModelForm()
    return render(request, 'help/support.html', {'form': form})


def language(request):
    languages = Language.objects.all()
    return render(request, 'languages.html', {'languages': languages})

def about_us(request):
    return render(request, 'about_us.html')