from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitLog
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    today = timezone.now().date()
    logs = {log.habit_id: log.completed for log in HabitLog.objects.filter(
        habit__in=habits, date=today)}
    return render(request, 'tracker/habit_list.html', {'habits': habits, 'logs': logs, 'today': today})


@login_required
def toggle_habit_log(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id, user=request.user)
    today = timezone.now().date()
    log, created = HabitLog.objects.get_or_create(habit=habit, date=today)
    log.completed = not log.completed
    log.save()
    return redirect('tracker:habit_list')
