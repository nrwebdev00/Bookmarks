from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm

@login_required
def dashboard(request):
    context = {'section':'dashboard'}
    return render(request, 'account/dashboard.html', context)

def user_login(request):
     if request.method == 'POST':
         form = LoginForm(request.POST)
         if form.is_valid():
             cd = form.cleaned_data
             user = authenticate(
                 request,
                 username=cd['username'],
                 password=cd['password']
             )
             if user is not None:
                 if user.is_active:
                     login(request, user)
                     return HttpResponse('Authenticated successfully')
             else:
                 return HttpResponse('Invalid Login')
         else:
             return HttpResponse('Disabled Account')
     else:
        form = LoginForm()
        context = {'name':'nathon', 'form':form, 'title':'Login'}
        return render(request, 'account/login.html', context)