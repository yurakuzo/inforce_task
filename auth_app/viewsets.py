from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import ValidationError
from .serializers import VoteSerializer, EmployeeSerializer, EmployeeRegisterSerializer
from .models import Vote, Employee
from main_app.models import Menu


class VoteViewSet(viewsets.ModelViewSet):
    """Basic Vote ViewSet"""

    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EmployeeViewSet(viewsets.ModelViewSet):
    """Basic Employee ViewSet"""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EmployeeRegisterViewSet(generics.CreateAPIView):
    """Employee Register ViewSet"""
    
    permission_classes = [permissions.AllowAny]
    queryset = Employee.objects.all()
    serializer_class = EmployeeRegisterSerializer
