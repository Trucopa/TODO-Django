from django.shortcuts import render
from rest_framework import viewsets
from task.models import Task 
from .serializer import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer