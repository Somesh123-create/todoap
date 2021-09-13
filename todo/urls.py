from django.urls import path
from .views import TaskView, TaskCreateView, TaskDeleteView, TaskUpdateView, TaskDetailView

urlpatterns = [
    path('', TaskView.as_view(), name='task_list' ),
    path('detail_task/<int:pk>', TaskDetailView.as_view(), name='detail_task'),
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='delete_task'),
    path('update_task/<int:pk>', TaskUpdateView.as_view(), name='update_task'),
]
