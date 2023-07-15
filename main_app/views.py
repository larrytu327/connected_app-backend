from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MessageBoardSerializer, AppUserSerializer
from .models import MessageBoard
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

class MessageBoardView(viewsets.ModelViewSet):
    serializer_class = MessageBoardSerializer
    queryset = MessageBoard.objects.all()

class AppUserView(viewsets.ModelViewSet):
    serializer_class = AppUserSerializer
    queryset = User.objects.all()