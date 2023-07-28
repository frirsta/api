from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User, TestRequirements, Test, TesterResult
from .serializers import UserSerializer, TestRequirementsSerializer, TesterResultSerializer, ResultSerializer, TestSerializer

# Create your views here.
class ClientList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer