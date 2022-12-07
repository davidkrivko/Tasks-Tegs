from django.urls import path

from task.views import index, TaskDetailView,\
    TaskCreateView, TaskUpdateView, TaskDeleteView,\
    TagListView, TagDetailView, TagUpdateView, TagDeleteView,\
    TagCreateView, task_done_changing, TaskListView


urlpatterns = [
    path("", index, name="index"),

    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("task/<int:pk>/done/", task_done_changing, name="task_done"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag_detail"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
]

app_name = "task"
