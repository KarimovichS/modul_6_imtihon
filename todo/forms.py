from django.forms import ModelForm

from .models import Todo


class todo_forms(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'content', 'important']
