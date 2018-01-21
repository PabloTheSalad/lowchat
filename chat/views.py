from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

# from django.urls import reverse

from .models import Message, Features

from .forms import LoginForm, RegistrateForm, MessageForm


@login_required(login_url='/login')
def profile(request):
    user = request.user
    return render(request, 'chat/profile.html', {'user': user})


def lin(request):
    error = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/chat')
            else:
                error = True
    return render(request, 'chat/login.html', {'error': error})


def lout(request):
    logout(request)
    return HttpResponseRedirect('/login')


@login_required(login_url='/login')
def chat(request):
    user = request.user
    messages = Message.objects.all()[:100]
    return render(request, 'chat/chat.html',
                  {'user': user, 'messages': messages})


@login_required(login_url='/login')
def sendMessage(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        text = form.data['text']
        if text:
            Message(user=request.user, text=text).save()
    return HttpResponseRedirect('/chat')


def registrate(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/chat')
    if request.method == 'POST':
        form = RegistrateForm(request.POST)
        data = form.data
        user_exist = User.objects.filter(username=data['username']).count()
        if form.is_valid():
            if user_exist:
                return render(request, 'chat/registrate.html',
                              {'error': 'This user is exist', 'form': form})
            user = User.objects.create_user(
                data['username'],
                data['email'],
                data['password']
            )
            Features(
                user=user,
                age=data['age'],
                gender=data['gender'],
                information=data['information']
            ).save()
            url = '/login'
        else:
            url = '/registrate'
        return HttpResponseRedirect(url)
    else:
        form = RegistrateForm()
        return render(request, 'chat/registrate.html', {'form': form})


@login_required(login_url='/login')
def otherwise(request, url='str'):
    return HttpResponseRedirect('/chat')
