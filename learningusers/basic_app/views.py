from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileInfoForm
from django.contrib.auth.models import User
### USER AUTH IMPORTS
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, template_name='basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Log out succesfull')
    return redirect('login')
    


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'You have been succesfully authenticated.')
            # return redirect('index')
            #http://www.learningaboutelectronics.com/Articles/How-to-redirect-a-user-after-login-to-the-URL-in-the-next-parameter-in-Django.php
            next_page = request.POST.get('next')
            return redirect(next_page) if next_page else  redirect('index')
        else:
            check_user = User.objects.filter(username=username)
            if check_user:
                messages.warning(request, 'Credentials are not correct.')
            else:
                messages.warning(request, f'We couldnot find any user named as {username}.')


    return render(request, 'basic_app/login.html')






def register(request):

    if request.method == 'POST':
        u_form = UserRegisterForm(data=request.POST)
        p_form = UserProfileInfoForm(data=request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            user.set_password(user.password)
            user.save()

            profile = p_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            messages.success(request, 'User Succesfully Created.')
            
            return redirect('login')  

        else:
            messages.warning(request, 'User NOT Created.')


    else:
        u_form = UserRegisterForm()
        p_form = UserProfileInfoForm()
    
    return render(request, template_name='basic_app/registration.html', context = dict(
        u_form=u_form,
        p_form=p_form,
    ))


@login_required
def about(request):
    return render(request, template_name='basic_app/about.html')