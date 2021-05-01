from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
import os, urllib.request
from django.core.files import File
from django.urls import reverse
# from django.core.validators import validate_comma_separated_integer_list
# from users.models import CustomUser
# import random

class CustomUserManager(BaseUserManager):
    """custom user manager class"""
    use_in_migration = True
    # email, nickname, role, company, team, pronouns,  password,
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ Custom user model class"""
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('email'), unique=True)
    main = models.ImageField(upload_to='users/', blank=True)
    # default="static/img/profile.png"
    image_url = models.URLField(blank=True)
    nickname = models.CharField(_('nickname'), max_length=50, blank=True)
    role = models.CharField(_('role'), max_length=100)
    company = models.CharField(_('company'), max_length=150, blank=True)
    team = models.CharField(_('team'), max_length=50, blank=True)
    pronouns = models.CharField(_('pronouns'), max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superadmin = models.BooleanField(_('is_superadmin'), default=False)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(default=True)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        """stirng representation"""
        return self.email

    def get_remote_image(self):
        if self.image_url and not self.main:
            result = urllib.request.urlretrieve(str(self.image_url))
            self.image_file.save(
                    os.path.basename(self.image_url),
                    File(open(result[0]))
                    )
            self.save()