from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserAccountSet, UserViewSet

router = routers.DefaultRouter()
# router.register('usersaccount', UserAccountSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
