from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from .models import Task
from .forms import CreateTaskForm, UpdateTaskForm


# Create your views here.


class TaskView(ListView):
    model = Task
    context_object_name = 'task'
    paginate_by = 10
    template_name = 'todo/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Task.objects.all().count()
        complete_task = Task.objects.filter(completed=True).count()
        remain_count = queryset - complete_task
        context['completed_count'] = complete_task
        context['task_count'] = queryset
        context['remain_count'] = remain_count
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'todo/create_task.html'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/delete_task.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'todo/update_task.html'
    success_url = reverse_lazy('task_list')
