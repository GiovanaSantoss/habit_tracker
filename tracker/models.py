from django.db import models
from django.contrib.auth.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    goal_type = models.CharField(max_length=20, choices=[
                                 ('daily', 'Diário'), ('weekly', 'Semanal')])
    target = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {'Feito' if self.completed else 'Não feito'}"
