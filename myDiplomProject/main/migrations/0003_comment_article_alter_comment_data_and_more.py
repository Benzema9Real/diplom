# Generated by Django 5.0.6 on 2024-05-21 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_category2_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.article'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=1000, verbose_name='Комментарий'),
        ),
    ]
