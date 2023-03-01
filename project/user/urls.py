from django.contrib import admin
from django.urls import path, include
from user.views import *

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('verify/', VerifyOTP.as_view())
]
