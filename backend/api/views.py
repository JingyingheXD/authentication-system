from django.shortcuts import render
from rest_framework import viewsets
from .models import UserAccount
from .serializers import UserAccountSerializer


class UserAccount(viewsets.UserAccount):
    queryset = UserAccount.objects.all()
    serilizer_class = (UserAccountSerializer, )
