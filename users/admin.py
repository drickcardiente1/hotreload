from django.contrib import admin
from .models import *
class example(admin.ModelAdmin):
        list_display = ('id', 'email', 'was_logedin', 'was_logedout')
        list_filter = ('id', 'email')
admin.site.register(activitie,example)

# Register your models here.
