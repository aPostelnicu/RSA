from django.shortcuts import render
from .models import Message
from .forms import MessageForm

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
