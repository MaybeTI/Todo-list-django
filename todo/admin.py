from django.contrib import admin
from django.contrib.auth.models import Group
from todo.models import Task, Tag


admin.site.unregister(Group)
admin.site.register(Task)
admin.site.register(Tag)
