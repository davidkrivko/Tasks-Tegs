from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from task.models import Tag, Task


def index(request):
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
    }

    return render(request, "task/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tag")


def task_done_changing(request, pk):
    task = Task.objects.get(pk=pk)

    task.done = not task.done
    task.save()

    return redirect("task:task_list")


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:task_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task_list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagDetailView(generic.DetailView):
    model = Tag


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag_list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag_list")
