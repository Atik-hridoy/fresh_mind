# fresh_mind/urls.py

from django.contrib import admin
from django.urls import path
from health_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('quote/', views.daily_quote, name='daily_quote'),
    path('mood/', views.mood_tracker, name='mood_tracker'),
    path('habit/', views.habit_tracker, name='habit_tracker'),
]
