from rest_framework import serializers
from register.models import Register
from verify.models import Verify

import random
from random import randint


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id','is_set_pw', 'firstname', 'lastname', 'email', 'phone', 'address_line_1','address_line_2','city','pin_code','photo','password','access_token','fb_id','fb_access_token','google_id','google_access_token','activation_key','activation_key_time')


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        activation_key = str(random.randint(100000, 999999)) 
        
        import datetime
        activation_key_time = datetime.datetime.now()

        objects=[]
                
        if(Register.objects.filter(is_set_pw=validated_data.get('is_set_pw') == 1)):
         if(Register.objects.filter(email=validated_data.get('email')).exists()):
          return validated_data
         else:
          from django.core.mail import send_mail
          send_mail('FoodRomeo: Confirm your Account.','Click on the link to confirm your account and set a password http://localhost/set-password/?activation_key='+activation_key+' The link expires in 48 hours.', 'poojapauskar22@gmail.com', [validated_data.get('email')], fail_silently=False)
          objects =Register.objects.create(**validated_data)
          Register.objects.filter(email=validated_data.get('email')).update(activation_key=activation_key,activation_key_time=activation_key_time)
          return objects
        else:
          if(Register.objects.filter(email=validated_data.get('email')).exists()):
           from django.core.mail import send_mail
           send_mail('FoodRomeo: Reset your password.','Click on the link to set a password http://localhost/set-password/?activation_key='+activation_key+' The link expires in 48 hours.', 'poojapauskar22@gmail.com', [validated_data.get('email')], fail_silently=False)
           Register.objects.filter(email=validated_data.get('email')).update(activation_key=activation_key,activation_key_time=activation_key_time)
           return validated_data
          else:
           return objects
        

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
        instance.save()
        return instance

