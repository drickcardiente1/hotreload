from django.shortcuts import render, redirect
from django.contrib.auth import logout, get_user_model, authenticate, login
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from core.models import *
from .signals import *
UserModel = get_user_model()

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def login_view(request):
    if request.user.is_authenticated:
            return redirect('home')
    else:
        return render(request, 'validation/login.html')


def sign_up_view(request):
    form = RegistrationForm()
    if request.user.is_authenticated:
            return redirect('home')
    else:
        return render(request, 'validation/register.html', {'form':form})

def sign_up_proccess(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('partials/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            return redirect('signup')
    else:
        return redirect('signup')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')

def login_request(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        messages.success(request, "LOGIN SUCCESSFULLY!")
        return redirect('home')
    else:
        messages.error(request, "INVALID CRIDINTIAL")
        return redirect('login')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return render(request, 'validation/register.html')

def notify(request):
    current_user = request.user
    note = activitie.objects.filter(email = current_user.id)
    return JsonResponse({"notif":list(note.values())})

def notify2(request):
    if request.user.is_anonymous():
        print("wala")
    else:
        print("naa")
        # user is anon user

# def save(request):
#     current_user = request.user
#     activitie.objects.filter(email = current_user.id).update(was_logedin = True)
#     return redirect('home')

# def check(request):
#     print("Refresh detected")
    # current_user = request.user
    # activitie.objects.filter(email = current_user.id).update(was_logedin = True)
    # return redirect('home')





