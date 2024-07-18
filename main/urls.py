from . import views
from django.urls import path

urlpatterns = [path('', views.main2, name='main2'),


               path('main/', views.main, name='main'),
               path('sport/', views.sport, name='sport'),
               path('cooking/', views.cooking, name='cooking'),
               path('scince/', views.scince, name='scince'),
               path('technic/', views.technic, name='technic'),
               path('help/', views.help, name='help'),
               path('support/', views.support, name='support'),
               path('successfully/', views.successfully, name='successfully'),
               path('create/', views.create, name='create'),
               path('registr/', views.registr, name='registr'),
               path('grade_forms/', views.grade_forms, name='grade_forms'),
               path('grade/', views.grade, name='grade'),
               path('login/', views.login, name='login'),
               path('about_us/', views.about_us, name='about_us'),
               path('language/', views.language, name='language'),
               path('<int:pk>/', views.MyDetailView.as_view(), name='detail')
               ]
