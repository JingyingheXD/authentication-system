from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserAccountSet

router = routers.DefaultRouter()
router.register('users', UserAccountSet)

urlpatterns = [
    path('', include(router.urls)),
]
