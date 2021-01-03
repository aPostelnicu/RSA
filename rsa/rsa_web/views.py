from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Message
from .forms import *
from .cipher import *

def home(request):
    context = {}
    criptate.clear()
    return render(request, "rsa_web/home.html", context)

def encryption(request):

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('resultE/')

    context = {
        'form': form
    }
    return render(request, "rsa_web/encryption.html", context)

def resultE(request):
    obj = Message.objects.latest('id')
    secret = criptare(obj.body, n, e)

    context = {
        'obj': obj, 'secret': secret
    }
    return render(request, "rsa_web/resultE.html", context)

def decryption(request):
    form = DecryptionForm()

    if request.method == 'POST':
        form = DecryptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('resultD/')

    context = {
        'form': form
    }
    return render(request, "rsa_web/decryption.html", context)

def resultD(request):

    obj = SecretMessage.objects.latest('id')
    secret = obj.msg
    text = decriptare(secret, n, d)

    context = {
        'obj': obj, 'text': text
    }
    return render(request, "rsa_web/resultD.html", context)
