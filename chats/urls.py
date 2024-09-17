from django.urls import path
from .views import *

app_name = "chats"

urlpatterns = [
    path('', question_view.as_view(), name='question'),
    path('chat', start_chat.as_view(), name='chat'),    
]