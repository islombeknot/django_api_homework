from django.shortcuts import render
from rest_framework import generics
from .models import User, RU, KZ, KG, US, KR, UZ
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.validators import ValidationError
from .utils import send_sms
from rest_framework.views import APIView
from rest_framework.response import Response

class UserListCreateAPIView(generics.ListCreateAPIView):


    queryset = User.objects.all()
    serializer_class = UserSerializer

class ResendVerifyView(APIView):
     permission_classes = (IsAuthenticated)

     def post(self, request):
          user = self.request.user
          if user.auth_type  == RU:
               code = user.create_confirmation_code(RU)
               send_sms(code)
          elif user.auth_type == KZ:
               code = user.create_confirmation_code(KZ)
               send_sms(code)
          elif user.auth_type == KG:
               code = user.create_confirmation_code(KG)
               send_sms(code)
          elif user.auth_type == KR:
               code = user.create_confirmation_code(KR)
               send_sms(code)
          elif user.auth_type == US:
               code = user.create_confirmation_code(US)
               send_sms(code)
          elif user.auth_type == UZ:
               code = user.create_confirmation_code(UZ)
               send_sms(code)
          else: 
                 data = {
                        "status":False,
                        "message":"siz bergan data xato"
                }
                 raise ValidationError(data)
          data = {
               "status":True,
               "message":"yuborildi"
          
          
          }
          return Response(data)