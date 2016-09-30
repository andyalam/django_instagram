from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from . forms import UserCreateForm
from . models import UserProfile, IGPost, Comment, Like


def index(request):
    posts = IGPost.objects.order_by('-posted_on')
    return render(request, 'feeds/index.html', {
        'posts': posts
    })


def signup(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'feeds/signup.html', {
        'form': form
    })


def login_user(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'feeds/login.html', {
        'form': form
    })


def signout(request):
    logout(request)
    return redirect('index')


def signup_success(request):
    return render(request, 'feeds/signup_success.html')


def profile(request, username):
    user = User.objects.filter(username=username)[0]
    profile = UserProfile.objects.filter(user=user)[0]

    context = {
        'username': username,
        'user': user,
        'profile': profile
    }
    return render(request, 'feeds/profile.html', context)
