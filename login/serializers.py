from rest_framework import serializers
from register.models import Register
from login.models import Login
from verify.models import Verify

import random
from random import randint

class StatusCode(object):
    OK = 200
    NOT_FOUND = 404
    # add more status code according to your need
import json
from django.http import HttpResponse
 
def JSONResponse(data = None, status = StatusCode.OK):
    if data is None:
        return HttpResponse(status)
    if data and type(data) is dict:
        return HttpResponse(json.dumps(data, indent = 4, encoding = 'utf-8', sort_keys = True), \
            mimetype = 'application/json', status = status)
    else:
        return HttpResponse(status = StatusCode.NOT_FOUND)

from django.views import generic
from django.views.generic import ListView

from register.models import Register
from rest_framework import generics


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('email','password')


    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     # Register.objects.all().delete()
    #     # Verify.objects.all().delete()
    #     # if Register.objects.filter(email=validated_data.get('email')).exists():
    #     #   return validated_data
    #     details=[]          
    #     if(Register.objects.filter(email=validated_data.get('email')).exists()):
    #      if(Register.objects.filter(password=validated_data.get('password')).exists()):
    #       details.append(
    #                       {
    #                         'valid':1,
    #                         'access_token':'abc',
                              
    #                       }
    #                 )
    #      else:
    #       details.append(
    #                       {
    #                         'status':401,
    #                         'message':'Invalid Password',
                              
    #                       }
    #                 )
    #     else:
    #       details.append(
    #                       {
    #                         'status':401,
    #                         'message':'Invalid Credentials',
                              
    #                       }
    #                 )  

    #     import sys

    #     from django.http import JsonResponse
    #     print >> sys.stderr, "details"
    #     print >> sys.stderr, JsonResponse(details,safe=False)

        
    #     return JsonResponse(details,safe=False)

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

