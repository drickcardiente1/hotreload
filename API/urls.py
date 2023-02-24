
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('verify/', verify_otp.as_view()),
    path('register/', Send_otp.as_view()),
]
