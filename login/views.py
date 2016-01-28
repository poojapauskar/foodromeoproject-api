from register.models import Register
from login.serializers import LoginSerializer
from rest_framework import generics

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

class LoginList(generics.ListCreateAPIView):
 def get(self, request, *args, **kwargs):
  object1=request.META.get('HTTP_EMAIL')
  details=[]
  import sys
  print >> sys.stderr, request.META.get('HTTP_EMAIL')          
  if(Register.objects.filter(email=request.META.get('HTTP_EMAIL')).exists()):
   if(Register.objects.filter(email=request.META.get('HTTP_EMAIL'),password=request.META.get('HTTP_PASSWORD')).exists()):
    from oauth2_provider.settings import oauth2_settings
    from oauthlib.common import generate_token
    from django.http import JsonResponse
    from oauth2_provider.models import AccessToken, Application, RefreshToken
    from django.utils.timezone import now, timedelta
    from django.http import HttpResponse
    from django.contrib.auth import login
    from datetime import datetime
    from django.contrib.auth.models import User, Group
    if(User.objects.filter(username=request.META.get('HTTP_EMAIL')).exists()):
     User.objects.filter(username=request.META.get('HTTP_EMAIL')).delete()
    else:
     pass
    user=User.objects.create(username=request.META.get('HTTP_EMAIL'),password="foodromeo")
    expire_seconds = oauth2_settings.user_settings['ACCESS_TOKEN_EXPIRE_SECONDS']
    scopes = oauth2_settings.user_settings['SCOPES']
    application = Application.objects.get(name="foodromeo")
    expires = datetime.now() + timedelta(seconds=expire_seconds)
    access_token = AccessToken.objects.create(
        user=user,
        application=application,
        token=generate_token(),
        expires=expires,
        scope=scopes)
    refresh_token = RefreshToken.objects.create(
        user=user,
        token=generate_token(),
        access_token=access_token,
        application=application)
    import json
    token = access_token.token
    token= json.dumps(token)
    token = token.replace('"','')
    Register.objects.filter(email=request.META.get('HTTP_EMAIL')).update(access_token=access_token.token)
    details.append(
                   {
                    'status':200,
                    'valid':1,
                    'access_token':access_token.token,
                   }
                  )
   else:
    details.append(
                   {
                    'status':401,
                    'message':'Invalid Password',
                   }
                  )  
  else:
   details.append(
                  {
                   'status':400,
                   'message':'Invalid Credentials',
                  }
                 )  

  import sys
  from django.http import JsonResponse
  return JsonResponse(details[0],safe=False)




class LoginDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Register.objects.all()
    serializer_class = LoginSerializer