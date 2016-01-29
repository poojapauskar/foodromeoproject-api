import httplib2
import urllib

from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import simplejson as json
from django.http import JsonResponse

from register.models import Register

from django.shortcuts import get_object_or_404
from django.db.models import Count 
from django.http import JsonResponse

from django.contrib.auth.models import User, Group



# class Get_listList(generics.ListCreateAPIView):
#  queryset = Ticket.objects.all()
#  serializer_class = Get_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

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
class CustomListView(generics.ListCreateAPIView):
    #paginate_by = 2
    def get(self, request, *args, **kwargs):
      fb_access_token = request.GET.get('fb_access_token')

      import json
      import sys
      print >> sys.stderr, "fb_access_token"
      print >> sys.stderr, fb_access_token

      
      http = httplib2.Http(timeout=15)
      # Get basic information about the person
      response, content = http.request('https://graph.facebook.com/me?fields=id,name,email,first_name,last_name,picture' \
          u'&access_token=%s' % fb_access_token)
      data = json.loads(content)

      # ('https://graph.facebook.com/me?fields=id,name,email,first_name,last_name,picture' \
      #     u'&access_token=%s' % fb_access_token)
   # ?fields=id,name,location,picture' \
   #        u'&access_token={1}


      import sys
      print >> sys.stderr, "response"
      print >> sys.stderr, response
      print >> sys.stderr, "data"
      print >> sys.stderr, data

      details=[]

      if (response['status'] == "200") :
        if(Register.objects.filter(fb_id=data['id']).exists()):
          obj=Register.objects.get(fb_id=data['id'])
          details.append(
                          {
                            'status':200,
                            'fb_id':data['id'],
                            'name':data['name'],
                            # 'fb_access_token':fb_access_token,
                            # 'expiry':response['expires'], 
                            'firstname':obj.firstname,
                            'lastname':obj.lastname,
                            
                            'picture':obj.photo,
                            'access_token':obj.access_token,
                            # 'data':data,
                            # 'response':response,
                            'email':obj.email,
                          }
                    )
        else:

          if(User.objects.filter(username=data['id']).exists()):
           User.objects.filter(username=data['id']).delete()



          user=User.objects.create(username=data['id'],password="foodromeo")

          from oauth2_provider.settings import oauth2_settings
          from oauthlib.common import generate_token
          from django.http import JsonResponse
          from oauth2_provider.models import AccessToken, Application, RefreshToken
          from django.utils.timezone import now, timedelta
          from django.http import HttpResponse
          from django.contrib.auth import login
         # from social.apps.django_app.utils import psa
         # from .tools import get_access_token
          from datetime import datetime


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

          # token = {
          #         'access_token': access_token.token,
          #         'token_type': 'Bearer',
          #         'expires_in': expire_seconds,
          #         'refresh_token': refresh_token.token,
          #         'scope': scopes}

          
          token = access_token.token
          token= json.dumps(token)
          token = token.replace('"','')

          # Register.objects.filter(email=validated_data.get('email')).update(access_token=token)

          Register.objects.create(access_token=token,fb_id=data['id'],fb_access_token=fb_access_token,email=data['email'],firstname=data['first_name'],lastname=data['last_name'],photo=data['picture']['data']['url'])
          

          details.append(
                          {
                            'status':200,
                            'fb_id':data['id'],
                            'name':data['name'],
                            'email':data['email'],
                            # 'fb_access_token':fb_access_token,
                            # 'expiry':response['expires'], 
                            'firstname':data['first_name'],
                            'lastname':data['last_name'],
                            'picture':data['picture']['data']['url'],
                            'access_token':token,
                            # 'data':data,
                          }
                    )
      else:
        details.append(
                        {
                          'status':400,
                          'message':"Invalid access token",
                        }
                  )

      #give an access token of our app and fb_id to client-end and save fb details in register model  
      from django.http import JsonResponse
      return JsonResponse(details[0],safe=False)

# def facebook(request):
#   params = {
#     'client_id': settings.FACEBOOK_APP_ID,
#     'redirect_uri': 'http://0.0.0.0:3000/facebook/',
#     'client_secret': settings.FACEBOOK_SECRET_KEY,
#     'code': request.GET['code']
#   }

#   http = httplib2.Http(timeout=15)
#   response, content = http.request('https://graph.facebook.com/oauth/access_token?%s' % urllib.urlencode(params))

  
#   # Find access token and expire (this is really gross)
#   params = content.split('&')

#   import sys
#   print >> sys.stderr, params
#   ACCESS_TOKEN = params[0].split('=')[1]
#   EXPIRE = params[1].split('=')[1]
  

#   # Get basic information about the person
#   response, content = http.request('https://graph.facebook.com/me?access_token=%s' % ACCESS_TOKEN)
#   data = json.loads(content)

#   # Try to find existing profile, create a new user if one doesn't exist
#   # try:
#   #   profile = Profileobjects.get(facebook_uid=data['id'])
#   # except ProfileDoesNotExist:
#   #   user = User.objects.create_user(data['username'], data['email'], data['id'])
#   #   profile = user.get_profile()
#   #   profile.facebook_uid = data['id']

#   # # Update token and expire fields on profile
#   # profile.facebook_access_token = ACCESS_TOKEN
#   # profile.facebook_access_token_expires = EXPIRE
#   # profile.save()

#   import sys
#   print >> sys.stderr, data
#   # print >> sys.stderr, data['username']
#   # print >> sys.stderr, data['email']
#   # print >> sys.stderr, data['phone']
#   # print >> sys.stderr, data['address']

#   # Authenticate and log user in
#   # user = authenticate(username=data['name'], password=data['id'])
#   # login(request, user)

#   user_details=[]
#   user_details.append(
#                   {
#                     'name':data['name'],
#                     'fb_id':data['id'],
#                     'access_token':ACCESS_TOKEN,
#                   }
#             )

#   return JsonResponse(user_details[0],safe=False)