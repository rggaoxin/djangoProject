from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user.serializers import *


class RegisterView(CreateAPIView):
    """
    用户注册
    """
    serializer_class = RegisterSerializer
    # permission_classes = (JSONWebTokenAuthentication,)


class UsernameValidateView(APIView):
    """
    校验用户名
    """
    def get(self, request, username):
        data_dict = {
            "username": username,
            "count": User.objects.filter(username=username).count()
        }
        return Response(data_dict)


class EmailValidateView(APIView):
    """
    校验email
    """
    def get(self, request, email):
        data_dict = {
            "email": email,
            "count": User.objects.filter(email=email).count()
        }
        return Response(data_dict)
