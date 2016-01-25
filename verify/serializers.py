from rest_framework import serializers
# from set_password.models import Set_password
from register.models import Register
from verify.models import Verify
from django.contrib.auth.models import User, Group


class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Verify
        fields = ('email','password','confirm_password','access_token','valid')


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        # Register.objects.filter(email=validated_data.get('email')).update(password=validated_data.get('password'))
        
        if (Verify.objects.filter(email=validated_data.get('email')).values('email')).exists():
         Verify.objects.filter(email=validated_data.get('email')).delete()


        

        user=User.objects.create(username=validated_data.get('email'),password="foodromeo")

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

        import json
        token = access_token.token
        token= json.dumps(token)
        token = token.replace('"','')

        Register.objects.filter(email=validated_data.get('email')).update(password=validated_data.get('password'),access_token=token)
        
        objects=Verify.objects.create(email=validated_data.get('email'),password=validated_data.get('password'),confirm_password=validated_data.get('confirm_password'),valid=1,access_token=token)
        import sys
        print >> sys.stderr, objects

        return objects

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address_line_1 = validated_data.get('address_line_1', instance.address_line_1)
        instance.address_line_2 = validated_data.get('address_line_2', instance.address_line_2)
        instance.city = validated_data.get('city', instance.city)
        instance.pin_code = validated_data.get('pin_code', instance.pin_code)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.password = validated_data.get('password', instance.password)
        instance.access_token = validated_data.get('access_token', instance.access_token)
        instance.confirmed = validated_data.get('confirmed', instance.confirmed)
        instance.save()
        return instance