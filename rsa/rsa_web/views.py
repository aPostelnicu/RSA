from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Message
from .forms import *
from .cipher import *

def home(request):
    context = {}
    return render(request, "rsa_web/home.html", context)

def encryption(request):
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('secret/')

    context = {
        'form': form
    }
    return render(request, "rsa_web/encryption.html", context)

def secret(request):
    obj = Message.objects.latest('id')
    secret = criptare(obj.body, n, e)

    context = {
        'obj': obj, 'secret': secret
    }
    return render(request, "rsa_web/secret.html", context)

def decryption(request):
    form = SecretMessageForm()

    if request.method == 'POST':
        form = SecretMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('message/')

    context = {
        'form': form
    }
    return render(request, "rsa_web/decryption.html", context)


def message(request):

    obj = SecretMessage.objects.latest('id')
    text = decriptare(obj.body, n, d)

    context = {
        'obj': obj, 'text': text
    }
    return render(request, "rsa_web/message.html", context)
