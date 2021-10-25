from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def validate_username(self, value):
        try:
            validate_email(value)
            return value
        except ValidationError as e:
            raise e
