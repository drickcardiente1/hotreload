from django.urls import path, include
from . import views
from . import signals

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.sign_up_view, name='signup'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('signup_proccess', views.sign_up_proccess, name='signup_proccess'),
    path('login_request', views.login_request, name='login_request'),
    path('notify', views.notify, name='notify'),
    # path('save', views.save, name='save'),
    # path('check', views.check, name='check'),
]