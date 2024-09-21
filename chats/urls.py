from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name = "chats"

urlpatterns = [
    path('question/', question_view.as_view(), name='question'),
    path('chat/', start_chat.as_view(), name='chat'),
    path('main/', main.as_view(), name='main'),
    path('login/', login.as_view(), name='login'),
    path('register/', register.as_view(), name='register'),
    path('findID/', find_ID.as_view(), name='findID'),
    path('findPW/', find_PW.as_view(), name='findPW'),
]