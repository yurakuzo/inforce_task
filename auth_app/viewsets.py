from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import ValidationError
from .serializers import VoteSerializer, EmployeeSerializer, EmployeeRegisterSerializer
from .models import Vote, Employee
from main_app.models import Menu


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRegisterViewSet(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Employee.objects.all()
    serializer_class = EmployeeRegisterSerializer
