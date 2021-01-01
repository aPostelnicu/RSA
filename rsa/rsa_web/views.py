from django.shortcuts import render
from .models import Message
from .forms import MessageForm
from .cipher import *

def main(request):
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, "rsa_web/index.html", context)

def getMessage(request):
    obj = Message.objects.latest('id')
    secret = criptare(obj.body, n, e)

    context = {
        'obj': obj, 'secret': secret
    }
    return render(request, "rsa_web/getMessage.html", context)
