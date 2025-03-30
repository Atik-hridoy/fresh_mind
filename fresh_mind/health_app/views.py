# views.py

from django.shortcuts import render
import random

# Dummy storage for simplicity (will be reset on server restart)
moods = []
habits = []

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
        mood = request.POST.get('mood')
        if mood:
            moods.append(mood)  # Add mood to the list
    return render(request, 'health_app/mood.html', {'moods': moods})

def habit_tracker(request):
    if request.method == 'POST':
        habit = request.POST.get('habit')
        if habit:
            habits.append(habit)  # Add habit to the list
    return render(request, 'health_app/habit.html', {'habits': habits})
