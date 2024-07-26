from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(),name='USER REGISTRATION'),
    path('login/',UserLoginView,name='USER LOGIN')   
]
