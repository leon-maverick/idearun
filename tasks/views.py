from .models import category, task
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View



class IndexView (generic.ListView):
	model = task
	template_name = "tasks/index.html"
	def get_queryset(self):
		return task.objects.order_by('creation_date').order_by('groups')

class TaskCreate (CreateView):
    model = task
    fields = ['title', 'creation_date', 'status', 'groups']
    success_url = reverse_lazy('tasks:home')

class TaskStatusUpdate (UpdateView):
    model = task
    fields = ['status']
    success_url = reverse_lazy('tasks:home')

class TaskUpdate (UpdateView):
    model = task
    fields = ['title', 'creation_date', 'status', 'groups']
    success_url = reverse_lazy('tasks:home')

class TaskDelete (DeleteView):
    model = task
    success_url = reverse_lazy('tasks:home')



