from django.shortcuts import render
from rest_framework import viewsets
from .models import UserAccount
from .serializers import UserAccountSerializer


class UserAccountSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
