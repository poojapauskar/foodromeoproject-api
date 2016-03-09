from rest_framework import serializers
# from set_password.models import Set_password
from register.models import Register
from verify.models import Verify
from django.contrib.auth.models import User, Group
# import settings.PUSH_NOTIFICATIONS_SETTINGS


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

        # Run on 2195 port & http://0.0.0.0:2195/device/apns/?access_token=hak7GAIRAi2iLL1KXqKyetSC3cjVko to register device
        from push_notifications.models import APNSDevice
        # 1a11266b8f923ef40e6f9dd425b957f21c5397e6
        # BEF62791B70AF1E44BB6F441DAF66C85608493250FCD8C7FE9116F1DAE978F5F
        device = APNSDevice.objects.get(registration_id='BEF62791B70AF1E44BB6F441DAF66C85608493250FCD8C7FE9116F1DAE978F5F')
        import sys
        print sys.stderr, "device"
        print sys.stderr, device
        device.send_message("You've got mail") # Alert message may only be sent as text.
        device.send_message(None, badge=5) # No alerts but with badge.
        device.send_message(None, badge=1, extra={"foo": "bar"}) # Silent message with badge and added custom data.

        # http://0.0.0.0:2195/verify/?access_token=hak7GAIRAi2iLL1KXqKyetSC3cjVko
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