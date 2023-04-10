from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from core.models import Employee

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    """
    ModelViewSet -> Contains all CRUD functionalities
    """
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()