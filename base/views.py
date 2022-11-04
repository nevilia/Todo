from django.shortcuts import render
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class TaskList(ListView):
    model = Task
    # template_name = 'task_list.html' #looks for template by this name by default because of generic view
    context_object_name = 'tasks'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__' #to bring out all fields taht are in createview 
    success_url = reverse_lazy('tasks')
    
class TaskUpdate(UpdateView):
    model=Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')