from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField('Название', max_length=50)
    category = models.CharField('Категория', max_length=50)
    text = models.TextField('Содержание')
    data = models.DateTimeField('Дата публикации',auto_now_add=True)
    email = models.EmailField('Email')
    my_image = models.ImageField(upload_to='images/')
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    text = models.CharField('Комментарий', max_length=300)
    email = models.EmailField('Email')
    data = models.DateTimeField('Дата')


class Support(models.Model):
    text = models.TextField('Ваша проблема')
    nomer = models.IntegerField('Ваш номер(без плюса)')
    data = models.DateTimeField('Дата')


class Grade(models.Model):
    grade = models.FloatField('Оценка',validators=[MaxValueValidator(5),MinValueValidator(1)])
    comment = models.TextField('Комментарий')
    email = models.EmailField('Email')

