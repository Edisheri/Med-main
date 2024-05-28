from django.urls import path

from main import views

app_name = 'main'


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('dost/', views.dost, name='dost'),
    path('kont/', views.kont, name='kont'),
]
