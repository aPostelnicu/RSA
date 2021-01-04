from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Message
from .forms import *
from .cipher import *

def home(request):
    criptate.clear()
    context = {}
    return render(request, "rsa_web/home.html", context)

def encryption(request):
    criptate.clear()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('result/')

    context = {
        'form': form
    }
    return render(request, "rsa_web/encryption.html", context)

def result(request):
    obj = Message.objects.latest('id')
    secret = criptare(obj.body, n, e)

    context = {
        'obj': obj, 'secret': secret
    }
    return render(request, "rsa_web/result.html", context)


def decryption(request):

    obj = Message.objects.latest('id')
    text = decriptare(criptate, n, d)

    context = {
        'obj': obj, 'text': text
    }
    return render(request, "rsa_web/decryption.html", context)
