from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from .models import Chat, Message


def main(request):
    # return render(request, 'chat/index.html')
    return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def user(request):
    return HttpResponseRedirect('/user/' + request.user.username + '/')


def userpage(request, username):
    user = request.user
    if username == user.username:
        this_user = True
    else:
        this_user = False

    return render(request, 'chat/userpage.html', {'user': user, 'this_user': this_user})


def lin(request):
    try:
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/user/' + user.username + '/')
        else:
            return render(request, 'chat/login.html', {'error': True})
    except:
        return render(request, 'chat/login.html')


def lout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def chats(request):
    user = request.user
    return render(request, 'chat/chats.html', {'user': user})


@login_required(login_url='/login')
def chat(request, chat_id):
    try:
        user = request.user
        chat = user.chat_set.get(pk=chat_id)
        return render(request, 'chat/chat.html', {'chat': chat, 'user': user})
    except (KeyError, Chat.DoesNotExist):
        return render(request, 'chat/error.html', {'error': 'This chat does not exist'})




