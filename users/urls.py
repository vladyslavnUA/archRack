from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('signup/', register, name='signup'),
    # SignupView.as_view()
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/', change_password, name='changep'),
    # path('oops-i-forgot/', iforgot, name='iforgot'),
    # path('oops-i-forgot/', auth_views.PasswordChangeView.as_view(template_name='users/forgot-password.html'), name='iforgot'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_reset_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/forgot-password.html', subject_template_name='users/password_reset_subject.txt', html_email_template_name='users/password_reset_email.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('logout/', logoutU, name='logout'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)