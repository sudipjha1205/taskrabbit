from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from.serializers import *

# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {
                    "message": "User registered successfully",
                    "user": serializer.data
                },
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def UserLoginView(request):
    serializer = UserLoginSerializers

    if serializer.is_valid():
        return Response({
            'token': serializer.validated_data['token']
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)

