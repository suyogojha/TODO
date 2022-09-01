from django.forms import ModelForm
from .models import Task

class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
