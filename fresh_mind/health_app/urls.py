from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quote/', views.quote, name='quote'),
    path('mood/', views.mood, name='mood'),
    path('mood/result/', views.mood_result, name='mood_result'),
    path('habit/', views.habit, name='habit'),
]
