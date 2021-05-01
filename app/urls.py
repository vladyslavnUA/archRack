from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('browse', browse, name='browse'),
    path('singleproject', singleproject, name='singleproject'),
    path('singlevideo', singlevideo, name='singlevideo'),
    path('myvids', myvids, name='myvids'),
    path('profile', profile, name='profile'),
    path('helpcenter', helpcenter, name='helpcenter'),
    path('videolist', videolist, name='videolist'),
    path('settings', setting, name='setting'),
    path('docs/new', newdoc, name='newdoc'),
    path('rand', rand, name='rand'),
    path('h', h, name='h'),
    path('projects/new', newproj, name='newproj'),
    path('projects/<slug:slug>', projdetail, name='projdetail'),
    path('docs/<slug:slug>', docdetail, name='docdetail'),
    path('<slug:slug>/e', editdoc, name='editdoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)