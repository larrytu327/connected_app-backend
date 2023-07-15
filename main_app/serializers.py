from rest_framework import serializers
from .models import MessageBoard
from django.contrib.auth import get_user_model

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('id', 'type', 'phone', 'address_line1', 'address_city', 'address_state', 'address_zip', 'birthdate', 'info', 'parents', 'teachers', 'students', 'classes', 'completed')

class MessageBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageBoard
        fields = ('id', 'subject', 'date_added', 'posts')

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model
        fields = ('user_id', 'email', 'username', 'type', 'phone', 'address_line1', 'address_city', 'address_state', 'address_zip', 'birthdate', 'info', 'parents', 'teachers', 'students', 'school', 'classes', 'completed')
