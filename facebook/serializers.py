from rest_framework import serializers
from register.models import Register


import httplib2
import urllib

from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import simplejson as json

from profiles.models import Profile
from django.http import JsonResponse


class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id', 'firstname', 'lastname', 'email', 'phone', 'address_line_1','address_line_2','city','pin_code','photo','password','access_token')


    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """

    #     if Register.objects.filter(email=validated_data.get('email')).exists():
    #       return validated_data

    #     from django.core.mail import send_mail
    #     send_mail('FoodRomeo: Confirm your Account.','Click on the link to confirm your account and set a password http://127.0.0.1:8000/verify/', 'poojapauskar22@gmail.com', [validated_data.get('email')], fail_silently=False)

        

    #     return Register.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.firstname = validated_data.get('firstname', instance.firstname)
    #     instance.lastname = validated_data.get('lastname', instance.lastname)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.address_line_1 = validated_data.get('address_line_1', instance.address_line_1)
    #     instance.address_line_2 = validated_data.get('address_line_2', instance.address_line_2)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.pin_code = validated_data.get('pin_code', instance.pin_code)
    #     instance.photo = validated_data.get('photo', instance.photo)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.access_token = validated_data.get('access_token', instance.access_token)
    #     instance.save()
    #     return instance