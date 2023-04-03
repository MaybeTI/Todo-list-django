from django.urls import path
from todo.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TagListView


urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/toggle/", TaskListView.as_view(), name="toggle-task"),
    path("tags/", TagListView.as_view(), name="tag-list")

]


app_name = "todo"
