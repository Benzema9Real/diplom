from django.contrib import admin
from .models import Article, Comment, Support, Grade, Language

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Support)
admin.site.register(Grade)
admin.site.register(Language)