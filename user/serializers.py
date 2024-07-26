from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserRegistrationSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,max_length=255)
    confirmPassword = serializers.CharField(write_only=True,max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirmPassword']
    
    def validate(self,data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError("Password do not match")
        return data

    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        return user

class UserLoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])

        if user:
            if not user.is_active:
                raise serializers.ValidationError("User is not active")
            return {
                'user': user,
                'token': Token.objects.get_or_create(user=user)[0].key
            }
        raise serializers.ValidationError("Invalid credentials")