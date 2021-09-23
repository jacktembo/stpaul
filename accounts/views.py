from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def register(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    else:
        form = User()
        form.username = request.POST.get('snumber', False)
        form.first_name = request.POST.get('fname', False)
        form.last_name = request.POST.get('lname', False)
        form.email = request.POST.get('email')
        form.password1 = request.POST.get('password', False)
        form.password2 = request.POST.get('password', False)
        try:
            form.save()
        except IntegrityError:
            return HttpResponse('user already exist')

        user = User.objects.get(username=form.username)
        user.set_password(form.password1)
        user.save()
        return HttpResponse('THANKS')


def login_view(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    else:
        username = request.POST.get('snumber', False)
        password = request.POST.get('login-password', False)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('logged in')
        else:
            return HttpResponse('incorrect username or password')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/accounts/login')
def dashboard(request):
    return HttpResponse('Dashboard')


@login_required(login_url='/accounts/login')
def password_change(request):
    if request.method != 'POST':
        return render(request, 'change_password.html')
    else:
        user = request.user
        entered = request.POST.get('current', False)  # The password a user enters as his current.
        new = request.POST.get('new', False)
        verify = request.POST.get('verify', False)  # The password confirmation.
        if user.check_password(entered) and new == verify:
            user.set_password(new)
            user.save()
            return HttpResponse('password changed')
        else:
            return HttpResponse('invalid entry')
