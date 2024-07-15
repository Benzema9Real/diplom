from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models




class Article(models.Model):
    Choices_list = (
        ('sport', 'спорт'),
        ('scince', 'наука'),
        ('cooking', 'кулинария'),
        ('technic', 'технологии'))

    title = models.CharField('Название', max_length=50)
    text = models.TextField('Содержание')
    category = models.CharField('Категория', max_length=50,choices=Choices_list)
    data = models.DateTimeField('Дата публикации', auto_now_add=True)
    email = models.EmailField('Email')
    my_image = models.ImageField(upload_to='images/')


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField('Комментарий', max_length=1000)
    email = models.EmailField('Email')
    data = models.DateTimeField('Дата',auto_now_add=True)


class Support(models.Model):
    text = models.TextField('Ваша проблема')
    nomer = models.IntegerField('Ваш номер(без плюса)')
    data = models.DateTimeField('Дата',auto_now_add=True)


class Grade(models.Model):
    grade = models.FloatField('Оценка', validators=[MaxValueValidator(5), MinValueValidator(1)])
    comment = models.TextField('Комментарий')
    email = models.EmailField('Email')

class Language(models.Model):
    name = models.CharField('Название', max_length=50)
    my_image = models.ImageField(upload_to='images/')
