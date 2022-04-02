from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

<<<<<<< HEAD

class UserProfileManager(BaseUserManager):
    """helps django work with our custom user model"""
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have email')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """creates and saves a new superuser with given details"""
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)


class Users(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    organizationName = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    zipCode = models.IntegerField(null=True)

    is_superuser = models.SmallIntegerField(db_column='is_superuser', blank=True, null=True)
    is_staff = models.SmallIntegerField(db_column='is_staff', blank=True, null=True)
    is_active = models.SmallIntegerField(db_column='is_active', blank=True, null=True)

    object = UserProfileManager()

    REQUIRED_FIELDS = ['email']
    PASSWORD_FIELD = 'password'
    USERNAME_FIELD = 'username'
    is_anonymous = False
    is_authenticated = True

    def get_short_name(self):
        """used to get a users short name"""
        return self.first_name

    def __str__(self):
        """Django uses this when it needs to convert the object into string"""
        return self.email

    class Meta:
        db_table = 'users'


class UserInfo(models.Model):
    username = models.CharField(max_length=100, default="")
=======
class UserInfo(models.Model):
    ##user = models.ForeignKey ##User, on_delete=models.CASCADE, null= True, blank=True)
>>>>>>> 4190f0ad9a4aa931423af86553a14a528381d7fe
    organizationName = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    zipCode = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Task(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField('date created')

    def __str__(self):
        return self.title
    
