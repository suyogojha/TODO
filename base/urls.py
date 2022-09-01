from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('taskform/', views.CreateTask,name='taskform'),
    path('taskcomplete/<str:pk>/', views.taskcomplete,name='taskcomplete'),
    path('edittask/<str:pk>/', views.Edittask,name='edittask'),
    path('taskcompleted/', views.task_comp,name='taskcompleted'),
]