from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.CharField(
        widget=forms.TextInput(attrs={"type": "date", "class": "form-control"})
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskFormToggle(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('is_done',)



