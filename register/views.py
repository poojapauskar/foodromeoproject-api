from register.models import Register
from register.serializers import RegisterSerializer
from rest_framework import generics

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

class RegisterList(generics.ListCreateAPIView):
 def get(self, request, *args, **kwargs):
  activation_key = str(random.randint(100000, 999999)) 
        
  import datetime
  activation_key_time = datetime.datetime.now()

                # from django.core.mail import send_mail
                # send_mail('FoodRomeo: Confirm your Account.','Click on the link to confirm your account and set a password http://localhost/set-password/?activation_key='+activation_key+' The link expires in 48 hours.', 'poojapauskar22@gmail.com', [validated_data.get('email')], fail_silently=False)

  objects=[]
  
  is_pw= request.META.get('HTTP_IS_SET_PW')
  import sys
  print >> sys.stderr, is_pw
    

  if(request.META.get('HTTP_IS_SET_PW') == '1'):
   if(Register.objects.filter(email=request.META.get('HTTP_EMAIL')).exists()):
    objects.append(
                  {
                   'status':400,
                   'message':'User already exists',
                  }
                 )
    from django.http import JsonResponse
    return JsonResponse(objects[0],safe=False)
   else:
    from django.core.mail import send_mail
    send_mail('FoodRomeo: Confirm your Account.','Click on the link to confirm your account and set a password http://localhost/set-password/?activation_key='+activation_key+' The link expires in 48 hours.', 'poojapauskar22@gmail.com', [request.META.get('HTTP_EMAIL')], fail_silently=False)
    objects1 =Register.objects.create(email=request.META.get('HTTP_EMAIL'),firstname=request.META.get('HTTP_FIRSTNAME'),lastname=request.META.get('HTTP_LASTNAME'),phone=request.META.get('HTTP_PHONE'),address_line_1=request.META.get('HTTP_ADDRESS_LINE_1'),address_line_2=request.META.get('HTTP_ADDRESS_LINE_2'),city=request.META.get('HTTP_CITY'),pin_code=request.META.get('HTTP_PIN_CODE'),photo=request.META.get('HTTP_PHOTO'),password=request.META.get('HTTP_PASSWORD'),access_token=request.META.get('HTTP_ACCESS_TOKEN'),fb_id=request.META.get('HTTP_FB_ID'),fb_access_token=request.META.get('HTTP_FB_ACCESS_TOKEN'),google_id=request.META.get('HTTP_GOOGLE_ID'),google_access_token=request.META.get('HTTP_GOOGLE_ACCESS_TOKEN'),activation_key=request.META.get('HTTP_ACTIVATION_KEY'),activation_key_time=request.META.get('HTTP_ACTIVATION_KEY_TIME'),is_set_pw=request.META.get('HTTP_IS_SET_PW'))
    import sys
    print sys.stderr, "objects1"
    print sys.stderr, objects1
    Register.objects.filter(email=request.META.get('HTTP_EMAIL')).update(activation_key=activation_key,activation_key_time=activation_key_time)
    objects.append(
                  {
                   'status':200,
                   'message':'Confirmation mail is sent to your email address',
                  }
                 )
    from django.http import JsonResponse
    return JsonResponse(objects[0],safe=False)
  else:
   if(Register.objects.filter(email=request.META.get('HTTP_EMAIL')).exists()):
    from django.core.mail import send_mail
    send_mail('FoodRomeo: Reset your password.','Click on the link to set a password http://localhost/set-password/?activation_key='+activation_key+' The link expires in 48 hours.', 'poojapauskar22@gmail.com', [request.META.get('HTTP_EMAIL')], fail_silently=False)
    Register.objects.filter(email=request.META.get('HTTP_EMAIL')).update(activation_key=activation_key,activation_key_time=activation_key_time)
    objects.append(
                  {
                   'status':200,
                   'message':'Reset mail is sent to your email address',
                  }
                 )
    from django.http import JsonResponse
    return JsonResponse(objects[0],safe=False)
   else:
    objects.append(
                  {
                   'status':400,
                   'message':'User does not exists',
                  }
                 )
    from django.http import JsonResponse
    return JsonResponse(objects[0],safe=False)


class RegisterDetail(generics.ListAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer