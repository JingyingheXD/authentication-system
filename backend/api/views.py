from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.http import Http404
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        raise Http404("not exist")

    def retrieve(self, request):
        raise Http404("not exist")

    def update(self, request):
        raise Http404("not exist")

    def destroy(self, request):
        raise Http404("not exist")


class MovieViewSet():
    queryset = Movie.objects.all()
    serializer_class = (MovieSerializer, )


class RatingSerializer():
    queryset = Rating.objects.all()
    serializer_class = (RatingSerializer, )
