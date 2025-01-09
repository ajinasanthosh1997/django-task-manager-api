
from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
   
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task-lc'),
    path('api/tasks/<slug:slug>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-rud'),
]
