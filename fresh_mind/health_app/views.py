from django.shortcuts import render, redirect
from .models import Mood, Habit
import random

def home(request):
    return render(request, 'health_app/home.html')

def daily_quote(request):
    quotes = [
        "Believe you can and you're halfway there.",
        "Take care of your body. It’s the only place you have to live.",
        "Happiness is not something ready-made. It comes from your own actions.",
        "You are stronger than you think."
    ]
    quote = random.choice(quotes)
    return render(request, 'health_app/quote.html', {'quote': quote})

def mood_tracker(request):
    if request.method == 'POST':
        mood_text = request.POST.get('mood')
        if mood_text:
            Mood.objects.create(mood=mood_text)  # Save to database
        return redirect('mood_tracker')
    
    moods = Mood.objects.all()  # Fetch moods from DB
    return render(request, 'health_app/mood.html', {'moods': moods})

def habit_tracker(request):
    if request.method == 'POST':
        habit_text = request.POST.get('habit')
        if habit_text:
            Habit.objects.create(habit=habit_text)  # Save to database
        return redirect('habit_tracker')

    habits = Habit.objects.all()  # Fetch habits from DB
    return render(request, 'health_app/habit.html', {'habits': habits})
