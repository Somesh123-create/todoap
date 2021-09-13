from django import forms
from .models import Task, Category

cat_choices = Category.objects.all().values_list('cat_name','cat_name')
item_choices = []

for item in cat_choices:
    item_choices.append(item)



class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','description', 'category_name']

        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'input-field'}),
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'category_name': forms.Select(choices=item_choices, attrs={'class': 'browser-default'}),
        }


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','description','completed']
