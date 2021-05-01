from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.utils import timezone
from .models import *
from .forms import *

def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form.fields)
        # password1, form.password2
        if form.is_valid():
            email = form.cleaned_data.get('email')
            image = form.cleaned_data.get('image_url')
            name = form.cleaned_data.get('name')
            main = form.cleaned_data.get('main')
            company = form.cleaned_data.get('company')
            role = form.cleaned_data.get('role')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            print(email)
            # user = 
            # CustomUser.objects.create(email=email, name=name, main=main, image_url=image, company=company, role=role, 
                                            # created_at=timezone.now(), updated_at=None, is_superadmin=False, is_active=True, is_staff=False, password1=password1, password2=password2 )
            messages.warning(request, 'Email has already been used.')
            # custom = CustomUser()
            # custom.name = email
            # custom.email
            # messages.warning(request, 'Your account expires in three days.')
            # user = form.save()
            form.save()
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password1)
            login(request, user)
            return redirect('dashboard')
        else:
            form = CreateUserForm()
            # email = form['email']
            # if email.exists:
            #     messages.warning(request, 'Email has already been used.')
            for msg in form.error_messages:
                print(msg)
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            print('made it back')

    # elif request.method == 'GET':
    form = CreateUserForm()
    context = {'form':form}
        # return render(request, 'users/register.html', context)
    return render(request, 'users/register.html', context)

# class SignupView(FormView):
#     """sign up user view"""
#     form_class = CreateUserForm
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('home')

#     def form_valid(self, form):
#         """ process user signup"""
#         user = form.save(commit=False)
#         user.save()
#         login(self.request, user)
#         if user is not None:
#             return HttpResponseRedirect(self.success_url)
#         else:
#             messages.add_message(self.request, messages.INFO, 'Wrong credentials\
#                                 please try again')
#             return HttpResponseRedirect(reverse_lazy('register'))
#         return super().form_valid(form)

class LoginView(FormView):
    """login view"""

    form_class = LoginForm
    success_url = reverse_lazy('dashboard')
    template_name = 'users/login.html'

    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data

        user = authenticate(username=credentials['email'],
                            password=credentials['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                Please try again')
            return HttpResponseRedirect(reverse_lazy('login'))

def loginU(request):
    if request.user.is_authenticated:
            return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            print('made it')
            return redirect('dashboard')
        else:
            print('didnt')
            messages.info(request, 'Username or Password is incorrect') 

    context = {}
    return render(request, 'users/login.html')

def iforgot(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('password_reset_done')
    else:
        print('error')
        return render(request, 'users/forgot-password.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/redo.html', {
        'form': form
    })


def logoutU(request):
    logout(request)
    return redirect('login')