from django.urls import path
from .views import *

urlpatterns = [
    path('upload-profile/',ProfileView,name="UPLOAD PROFILE")
]
