from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('registrate/', views.registrate, name='registrate'),
    path('login/', views.lin, name='login'),
    path('logout/', views.lout, name='logout'),
    path('chat/', views.chat, name='chat'),
    path('chat/send/', views.sendMessage, name='send'),
    path('', views.otherwise, name='main'),
    path('<str:url>/', views.otherwise, name='otherwise')
]
