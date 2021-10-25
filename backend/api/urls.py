from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserAccountSerializer

router = routers.DefaultRouter()
router.register('users', UserAccountSerializer)

urlpatterns = [
    path('', include(router.urls)),
]
