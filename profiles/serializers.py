from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

class ProfileSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True,required=False)

    class Meta:
        model = Profile
        fields = ['user', 'emp_id','bio','designation','joined_at','image']

    def validate_image(self,value):
        if value.size > 5 * 1024 * 1024: #5 MB limit
            raise serializers.ValidationError("Image size can not be bigger than 5 MB")
        if value.image.width > 300 or value.image.height > 300:
            raise serializers.ValidationError("Image dimensions should be lower than 300")
        return value

    def create(self,validated_data):
        profile = Profile.objects.create(**validated_data)
        return profile
