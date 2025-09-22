from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('log/<int:habit_id>/', views.toggle_habit_log, name='toggle_habit_log'),
]
