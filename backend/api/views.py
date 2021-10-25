from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserAccountSet(viewsets.ModelViewSet):
#     queryset = UserAccount.objects.all()
#     serializer_class = UserAccountSerializer

#     # TODO restrict password format and content
#     @action(detail=False, methods=['POST'])
#     def create_account(self, request, pk=None):
#         # Incomplete input
#         if 'email' not in request.data and 'password' in request.data:
#             response = {'message': 'You need to provide an email'}
#             return Response(response, status=status.HTTP_400_BAD_REQUEST)
#         elif 'password' not in request.data and 'email' in request.data:
#             response = {'message': 'You need to set a password'}
#             return Response(response, status=status.HTTP_400_BAD_REQUEST)
#         elif 'email' not in request.data and 'password' not in request.data:
#             response = {
#                 'message': 'You need to provdie an email and set a password'}
#             return Response(response, status=status.HTTP_400_BAD_REQUEST)

#         # Complete input
#         else:
#             email = request.data['email']
#             # Don't allow repeat emails
#             if UserAccount.objects.filter(email=email).exists():
#                 response = {'message': 'Email exists'}
#                 return Response(response, status=status.HTTP_400_BAD_REQUEST)

#             else:
#                 password = request.data['password']
#                 userAccount = UserAccount.objects.create(
#                     email=email, password=password)
#                 serializer = UserAccountSerializer(userAccount, many=False)
#                 response = {'message': 'Account created',
#                             'result': serializer.data}
#                 return Response(response, status=status.HTTP_200_OK)
