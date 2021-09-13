from django.db import models
from django.urls import reverse



# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.cat_name



class Task(models.Model):
    task_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True,null=True, max_length=255)
    task_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        ordering = ["-task_date"]
        verbose_name_plural = "Task"

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
    # return reverse('article', args=(str(self.id)))
        return reverse('task_list')
