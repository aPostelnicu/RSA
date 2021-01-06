from django.forms import ModelForm
from .models import *

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['author', 'title', 'body']

class SecretMessageForm(ModelForm):
    class Meta:
        model = SecretMessage
        fields = ['body']
