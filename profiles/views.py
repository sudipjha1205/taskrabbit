from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from .models import Profile
from .serializers import *
# Create your views here.

class ProfileView(generics.CreateAPIView):
    serializer_class = ProfileSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {
                    "message": "Profile created successfully",
                    "profile": serializer.data
                },
                status=status.HTTP_201_CREATED,
                headers=headers
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)