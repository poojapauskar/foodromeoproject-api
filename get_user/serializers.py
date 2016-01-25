from rest_framework import serializers
from get_user.models import Get_user, LANGUAGE_CHOICES, STYLE_CHOICES
from register.models import Register




class Get_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('email','activation_key_time')
    
    

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.vz_id = validated_data.get('vz_id', instance.vz_id)
    #     instance.user_details = validated_data.get('user_details', instance.user_details)
    #     instance.question = validated_data.get('question', instance.question)
    #     instance.item_photo = validated_data.get('item_photo', instance.item_photo)
    #     instance.item = validated_data.get('item', instance.item)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.date_created = validated_data.get('date_created', instance.date_created)
    #     instance.date_validity = validated_data.get('date_validity', instance.date_validity)
    #     instance.ticket_id = validated_data.get('ticket_id', instance.ticket_id)
    #     instance.save()
    #     return instance

