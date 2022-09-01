from django.contrib import admin
from .models import Task, Category , Taskcompleted

# Register your models here.
admin.site.register(Task)
admin.site.register(Taskcompleted)
admin.site.register(Category)