from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [path('', views.main, name='main'),
               path('sport/', views.sport, name='sport'),
               path('cooking/', views.cooking, name='cooking'),
               path('scince/', views.scince, name='scince'),
               path('technic/', views.technic, name='technic'),
               path('help/', views.help, name='help'),
               path('support/', views.support, name='support'),
               path('create/', views.create, name='create'),
               path('registr/', views.registr, name='registr'),
               path('grade_forms/', views.grade_forms, name='grade_forms'),
               path('grade/', views.grade, name='grade'),
               path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
               path('<slug:slug>/', views.MyDetailView.as_view(), name='mydetail')
               ]
