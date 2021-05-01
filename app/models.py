from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
import os, urllib.request
from django.core.files import File
from django.urls import reverse
# from tinymce.models import HTMLField
from users.models import CustomUser
from ckeditor.fields import RichTextField

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# name, description, collaborators, rackdocs, slug, owner, created_at, updated_at, 
class Project(models.Model):
    """Project model for organizations"""
    name = models.CharField(_('name'), max_length=250, unique=True)
    description = models.TextField(_('description'), max_length=550)
    collaborators = models.ManyToManyField('users.CustomUser', related_name="proj_collaborators")
    rackdocs = models.ManyToManyField('RackDoc', related_name="project_rackdocs", blank=True)
    slug = models.SlugField(default='', editable=True, max_length=455, null=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
        }
        return reverse('projdetail', kwargs=kwargs)

    def __str__(self):
        return self.name

class RackDoc(models.Model):
    """ Custom user model class"""
    name = models.CharField(_('name'), max_length=100, unique=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    # email = models.EmailField(_('email'), unique=True)
    # content = HTMLField()
    content = RichTextField(blank=True, config_name='default')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    collaborators = models.ManyToManyField(CustomUser, related_name="doc_collaborators")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(default='', editable=True, max_length=455, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name', 'role']
    # objects = CustomUserManager()

    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')

    def get_remote_image(self):
        if self.image_url and not self.main:
            result = urllib.request.urlretrieve(str(self.image_url))
            self.image_file.save(
                    os.path.basename(self.image_url),
                    File(open(result[0]))
                    )
            self.save()

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
        }
        return reverse('docdetail', kwargs=kwargs)

    def __str__(self):
        return self.name

# class Company(models.Model):
#     """Company model for organizations"""
#     name = models.CharField(_('name'), max_length=250, unique=True)
#     about = models.TextField(_('about'), max_length=850)
#     members = models.ManyToManyField('users.CustomUser', related_name="company_members")
#     profile = models.ManyToManyField('Project', related_name="company_projects", blank=True)
#     rackdocs = models.ManyToManyField('RackDoc', related_name="company_rackdocs", blank=True)
#     slug = models.SlugField(editable=True, max_length=455, null=False)
#     owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def get_absolute_url(self):
#         kwargs = {
#             'slug': self.slug,
#         }
#         return reverse('projdetail', kwargs=kwargs)

#     def __str__(self):
#         return self.name