from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from todo.forms import TaskForm, TaskFormToggle
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskFormToggle(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            if task.is_done:
                task.is_done = False
            else:
                task.is_done = True
            task.save()
        return redirect("todo:home")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:home")


class TagListView(generic.ListView):
    model = Tag
