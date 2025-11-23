# daftarsanggar/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sanggar/<str:sanggar_id>/', views.detail, name='detail'),
    
]