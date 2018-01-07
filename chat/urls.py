from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.main, name='main'),
    path('user/', views.user, name='user'),
    path('user/<str:username>/', views.userpage, name='userpage'),
    path('login/', views.lin, name='login'),
    path('logout/', views.lout, name='logout'),
    path('chat/', views.chats, name='chats'),
    path('chat/<int:chat_id>/', views.chat, name='chat'),
]
