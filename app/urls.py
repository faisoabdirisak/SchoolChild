from django.urls import path;
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('activities/', views.activities, name='activities'),
    path('next/', views.next, name='next'),
    path('activity/<str:pk>/', views.activity, name='activity'),
    
]