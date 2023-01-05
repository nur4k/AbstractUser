from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializer
from .models import CustomUser


class CustomUserView(generics.ListAPIView):
    queryset = CustomUser
    serializer_class = CustomUserSerializer
