from asyncio.windows_events import NULL
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from .models import *

@receiver(user_logged_in)
def user_was_loged_in(sender, request, user, **kwargs):
    current_user = request.user
    active = activitie.objects.filter(email = current_user.id)
    if active:
        active.update(was_logedin = True, was_logedout = False)
    else:
        activitie.objects.create(email = current_user)

@receiver(user_logged_out)
def user_was_loged_out(sender, request, user, **kwargs):
    current_user = request.user
    active = activitie.objects.filter(email = current_user.id)
    active.update(was_logedin = False, was_logedout = True)
    print("logedout")
    # current_user = request.user
    # active = activitie.objects.filter(email = current_user.id)
    # if active:
    #     active.update(was_logedout = True, was_logedin = False)
    # else:
    #     activitie.objects.create(email = current_user)
    # current_user = request.user
    # active = activitie.objects.filter(email = current_user.id)
    # active.update(was_logedin = False, was_logedout = True)

# @receiver(user_login_failed)
# def user_was_loged_in_failed(sender, credentials , request, user, **kwargs):
#     print("user login failed")