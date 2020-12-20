from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm


# Create your views here.

def home(request):
    task = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'task':task,'form':form}

    return render(request, 'home.html', context)

def updateTask(request, pk):
    task1 = Task.objects.get(id=pk)
    form = TaskForm(instance=task1)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task1)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}


    return render(request, 'update.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')


    context = {'item':item}
    return render(request, 'delete.html',context)


