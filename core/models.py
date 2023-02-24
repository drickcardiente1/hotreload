from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
now = timezone.now()




# choices types
class Types(models.TextChoices):
        ADMIN = "ADMIN" , "admin"
        CLIENTS = "CLIENTS" , "clients"

# accounts manager
class UserAccountManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_admin, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,is_staff=is_staff,is_active=True,is_admin=is_admin,last_login=now,date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, username, email, password, **extra_fields):
        if not email or len(email) <= 0 :
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        user = self._create_user(username, email, password, False, False, **extra_fields)
        self.is_client = True
        self.is_admin = False
        self.is_staff = False
        self.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True, **extra_fields)
        self.is_client = False
        self.is_admin = True
        self.is_staff = True
        self.is_superuser = True
        return user

class account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=254, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_client = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True )
    type = models.CharField(max_length = 8 , choices = Types.choices , default=Types.ADMIN)
    date_joined = models.DateTimeField(auto_now_add=True)
    otp = models.CharField(max_length=6 , null=True, blank=True)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
    objects = UserAccountManager()
    def __str__(self):
        return str(self.email)
    def has_perm(self , perm, obj = None):
        return self.is_admin

    def has_module_perms(self , app_label):
        return True
    def save(self , *args , **kwargs):
        if self.type == Types.ADMIN :
            self.is_client = False
            self.is_admin = True
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_client = True
            self.is_admin = False
            self.is_staff = False
            self.is_superuser = False
        return super().save(*args , **kwargs)


# client Manager
class ClientManager(models.Manager):
    def create_user(self, username, email, password, **extra_fields):
        if not email or len(email) <= 0 :
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        user = self._create_user(username, email, password, False, False, **extra_fields)
        self.is_client = True
        self.is_admin = False
        self.is_staff = False
        self.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user
    def get_queryset(self , *args,  **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = Types.CLIENTS)
        return queryset

# client
class client(account):
    class Meta :
        proxy = True
    objects = ClientManager()
    def save(self , *args , **kwargs):
        self.is_client = True
        self.is_admin = False
        self.is_staff = False
        self.is_superuser = False
        return super().save(*args , **kwargs)
    


# Admin Manager
class AdminManager(models.Manager):
    def get_queryset(self , *args , **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = Types.ADMIN)
        return queryset

# Admin
class administrator(account):
    class Meta :
        proxy = True
    objects = AdminManager()
    def save(self  , *args , **kwargs):
        self.type = Types.ADMIN
        self.is_admin = True
        self.is_staff = True
        self.is_superuser = True
        return super().save(*args , **kwargs)
    