import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from imagekit.models import ProcessedImageField

from . forms import UserCreateForm, PostPictureForm, ProfileEditForm
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

            user = User.objects.get(username=request.POST['username'])
            profile = UserProfile(user=user)
            profile.save()
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
    user = User.objects.get(username=username)
    if not user:
        return redirect('index')

    profile = UserProfile.objects.get(user=user)
    context = {
        'username': username,
        'user': user,
        'profile': profile
    }
    return render(request, 'feeds/profile.html', context)


@login_required
def profile_settings(request, username):
    user = User.objects.get(username=username)
    if request.user != user:
        return redirect('index')

    if request.method == 'POST':
        print(request.POST)
        form = ProfileEditForm(request.POST, instance=user.userprofile, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile', kwargs={'username': user.username}))
    else:
        form = ProfileEditForm(instance=user.userprofile)

    context = {
        'user': user,
        'form': form
    }
    return render(request, 'feeds/profile_settings.html', context)


@login_required
def post_picture(request):
    if request.method == 'POST':
        form = PostPictureForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = IGPost(user=request.user,
                          title=request.POST['title'],
                          image=request.FILES['image'],
                          posted_on=datetime.datetime.now())
            post.save()
            return redirect(reverse('profile', kwargs={'username': request.user.username}))
    else:
        form = PostPictureForm()

    context = {
        'form': form
    }
    return render(request, 'feeds/post_picture.html', context)


def post(request, pk):
    post = IGPost.objects.get(pk=pk)
    print(post)
    context = {
        'post': post
    }
    return render(request, 'feeds/post.html', context)
