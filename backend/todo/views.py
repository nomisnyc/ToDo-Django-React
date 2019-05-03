# viewsets base class provides the implementation for CRUD operations by default, need to specify the serializer class and the query set

from django.shortcuts import render
from rest_framework import viewsets     
from .serializers import TodoSerializer 
from .models import Todo                

class TodoView(viewsets.ModelViewSet):  
    serializer_class = TodoSerializer    
    queryset = Todo.objects.all() 