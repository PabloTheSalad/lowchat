from django.shortcuts import render, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, JsonResponse

# from django.urls import reverse

from .models import Message, Features

from .forms import LoginForm, RegistrateForm, MessageForm

from django.utils import timezone


@login_required(login_url='/login')
def profile(request, user):
    html = 'profile.html'
    cur_username = request.user.username
    if (cur_username == user):
        html = 'current_profile.html'

    user = get_object_or_404(User, username=user)
    return render(request, 'chat/'+html, {'user': user})


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
    # Опасность при нуле сообщений!
    lm_id = Message.objects.last().id
    user.features.lr_message = lm_id
    lm = lm_id - 100
    if lm < 0:
        lm = 0
    messages = Message.objects.filter(id__gt=lm)
    request.user.features.last_enter = timezone.now()
    request.user.features.save()
    users_online = User.objects.filter(
        features__last_enter__gt=timezone.now()-timezone.timedelta(seconds=300)
    )
    return render(request, 'chat/chat.html',
                  {'user': user, 'users': users_online, 'messages': messages})


@login_required(login_url='/login')
def json_message(request, number):
    lm_id = Message.objects.last().id
    messages = Message.objects.filter(id__gt=lm_id-number)
    json = {}
    for message in messages:
        json[message.id] = {'username': message.user.username,
                            'time': message.gettime(), 'text': message.text}

    return JsonResponse(json, safe=False)


@login_required(login_url='/login')
def lm_json(request):
    user = request.user
    messages = Message.objects.filter(id__gt=user.features.lr_message)
    json = {}
    for message in messages:
        json[message.id] = {'username': message.user.username,
                            'time': message.gettime(),
                            'text': message.text
                            }

    return JsonResponse(json, safe=False)


@login_required(login_url='/login')
def sendMessage(request):
    form = MessageForm(request.POST)
    if form.is_valid():           # Здесь раньше была проверка на длинну текста
        Message(user=request.user, text=form.data['text']).save()
    return HttpResponseRedirect('/chat')


def change_theme(request):
    if request.user.is_authenticated:
        user = request.user
        if user.features.theme == 0:
            request.user.features.theme = 1
        else:
            request.user.features.theme = 0
        request.user.features.save()
        return JsonResponse({'status': 'ok'}, safe=False)
    else:
        return JsonResponse({'status': 'not authenticated'}, safe=False)


def registrate(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/chat')
    if request.method == 'POST':
        form = RegistrateForm(request.POST, request.FILES)
        data = form.data
        # for d in data:
        #    print(d + ':' + data[d])
        # print(form.is_valid())
        # print(form.errors)
        # print(form.files)
        user_exist = User.objects.filter(username=data['username']).count()
        if form.is_valid():
            if user_exist:
                return render(request, 'chat/registrate.html',
                              {'error': 'This user is exist'})
            user = User.objects.create_user(
                data['username'],
                data['email'],
                data['password']
            )
            Features(
                user=user,
                age=data['age'],
                gender=data['gender'],
                information=data['information'],
                namecolor=data['namecolor'],
                image=form.files['image']
            ).save()
            url = '/login'
        else:
            url = '/registrate'
        return HttpResponseRedirect(url)
    else:
        return render(request, 'chat/registrate.html')


@login_required(login_url='/login')
def otherwise(request, url='str'):
    return HttpResponseRedirect('/chat')

