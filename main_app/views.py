from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer, MessageBoardSerializer
from .models import Profile, MessageBoard

# Create your views here.

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class MessageBoardView(viewsets.ModelViewSet):
    serializer_class = MessageBoardSerializer
    queryset = MessageBoard.objects.all()
