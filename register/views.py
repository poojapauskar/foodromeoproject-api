from register.models import Register
from register.serializers import RegisterSerializer
from rest_framework import generics


class RegisterList(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class RegisterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer