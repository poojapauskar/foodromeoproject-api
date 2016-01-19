from verify.models import Verify
from verify.serializers import VerifySerializer
from rest_framework import generics


class VerifyList(generics.ListCreateAPIView):
    queryset = Verify.objects.all()
    serializer_class = VerifySerializer


class VerifyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Verify.objects.all()
    serializer_class = VerifySerializer