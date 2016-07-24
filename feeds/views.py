from django.shortcuts import render, redirect
from django.http import HttpResponse

from . forms import UserCreateForm


def index(request):
    return render(request, 'feeds/index.html')


def signup(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')

    return render(request, 'feeds/signup.html', {
        'form': form
    })


def signup_success(request):
    return render(request, 'feeds/signup_success.html')