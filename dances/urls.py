from django.urls import path
from . import views

app_name = 'dances'

urlpatterns = [
    path('', views.dance_list, name='dance_list'),
    path('<int:dance_id>/', views.dance_detail, name='dance_detail'),
    path('<int:dance_id>/tutorial/', views.dance_tutorial, name='dance_tutorial'),
    path('<int:dance_id>/assessment/', views.dance_assessment, name='dance_assessment'),
    path('<int:dance_id>/result/', views.dance_result, name='dance_result'),
]
