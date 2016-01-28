from rest_framework import serializers
# from set_password.models import Set_password
from register.models import Register
from verify.models import Verify
from django.contrib.auth.models import User, Group


class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Verify
        fields = ('email','password','confirm_password','valid')


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        Register.objects.filter(email=validated_data.get('email')).update(password=validated_data.get('password'))
        
        objects=Verify.objects.create(email=validated_data.get('email'),password=validated_data.get('password'),confirm_password=validated_data.get('confirm_password'),valid=1)
        import sys
        print >> sys.stderr, objects

        Register.objects.filter(email=validated_data.get('email')).update(activation_key='')

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