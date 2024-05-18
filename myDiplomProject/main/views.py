from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Article, Grade
from .forms import ArticleModelForm, RegisterForm, GradeModelForm, SupportModelForm


def main(request):
    return render(request, 'main.html')


def sport(request):
    sports = Article.objects.filter(category='спорт')
    return render(request, 'topic/sport.html', {'sports': sports[::-1]})


def scince(request):
    scinces = Article.objects.filter(category='наука')
    return render(request, 'topic/scince.html', {'scinces': scinces[::-1]})


def cooking(request):
    cookings = Article.objects.filter(category='кулинария')
    return render(request, 'topic/cooking.html', {'cookings': cookings[::-1]})


def technic(request):
    technics = Article.objects.filter(category='технологии')
    return render(request, 'topic/technic.html', {'technics': technics[::-1]})


def help(request):
    return render(request, 'help/help.html')


def support(request):
    return render(request, 'help/support.html')


class MyDetailView(DetailView):
    model = Article
    template_name = 'detail/detail.html'
    context_object_name = 'article'



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
            return redirect('support')

    else:
        form = SupportModelForm()
    return render(request, 'help/support.html', {'form': form})