
from django.shortcuts import render, redirect
from django.contrib.auth import login

from account.forms import SignUpForm


def index(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/index.html')

    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'account/sign-up.html', context)

def tbk(request):
   return render(request, 'root.txt')
