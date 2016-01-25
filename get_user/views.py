from register.models import Register
from get_user.serializers import Get_userSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404


class Get_userDetail(generics.ListAPIView):
 serializer_class = Get_userSerializer

 def get_queryset(self):
  activation_key = self.kwargs['activation_key']

  objects=Register.objects.filter(activation_key=activation_key) 
  

  return objects


       

