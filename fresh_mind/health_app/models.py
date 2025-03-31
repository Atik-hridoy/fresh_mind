from django.db import models

class Mood(models.Model):
    mood = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mood

class Habit(models.Model):
    habit = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.habit
