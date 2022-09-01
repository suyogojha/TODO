from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category,on_delete=models.RESTRICT, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Taskcompleted(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
