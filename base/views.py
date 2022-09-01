from django.shortcuts import render,redirect
from .models import  Task, Category, Taskcompleted
from .forms import Taskform

# Create your views here.
def home(request):
    categories = Category.objects.all()
    if request.method == "GET":
        q = request.GET.get('q','') # This gets the date from the request which has name 'q'.
        task = Task.objects.filter(category__name = q) 
    content = {'task':task,'categories':categories}
    return render(request,'index.html',content)

def CreateTask(request):
    form = Taskform()
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    content = {'form':form}
    return render(request,'task_form.html',content)

def Edittask(request,pk):
    task = Task.objects.get(id=pk)
    form = Taskform(instance=task)
    if request.method == 'POST':
        category_name = request.POST.get('category')
        category  = Category.objects.get(id = category_name)
        task.name = request.POST.get('name')
        task.category = category
        task.save()
        return redirect('home')
    content = {'form':form}
    return render(request,'task_form.html',content)

def taskcomplete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('home')

def task_comp(request):
    task_complete = Taskcompleted.objects.all()
    content = {'task_complete':task_complete}
    return render(request,'task_complete.html',content)