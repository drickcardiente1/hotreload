from django.core.mail import send_mail
import random
from django.conf import settings
from core.models import *
from django.utils.crypto import get_random_string

def send_otp(email):
    user_obj = client.objects.get(email = email)
    subject = "Your account verification email"
    otp = get_random_string(length=6, allowed_chars='1234567890')
    message = f"Your otp is {otp}"
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    user_obj.otp = otp
    user_obj.save()