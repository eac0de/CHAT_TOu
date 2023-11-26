from django.contrib import admin
from django.urls import path

from chat import views
from chat.apps import ChatConfig

app_name = ChatConfig.name

urlpatterns = [
    path('chat/<int:room_id>', views.ChatView.as_view(), name='chat'),
    path('auth/', views.AuthView.as_view(), name='auth'),
    path('register/', views.RegisterView.as_view(), name='register')
]
