from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('profile/<str:user>', views.profile, name='profile'),
    path('registrate/', views.registrate, name='registrate'),
    path('login/', views.lin, name='login'),
    path('logout/', views.lout, name='logout'),
    path('chat/', views.chat, name='chat'),
    path('chat/json/<int:number>', views.json_message, name='json_message'),
    path('chat/json/lm', views.lm_json, name='last_messages'),
    path('chat/send/', views.sendMessage, name='send'),
    path('changetheme/', views.change_theme, name='change_theme'),
    path('', views.otherwise, name='main'),
    path('<str:url>/', views.otherwise, name='otherwise')
]
