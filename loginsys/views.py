from django.shortcuts import render, get_object_or_404  # render page, return data or 404 page
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username',)
        password = request.POST.get('password', )
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            login_error = 'User not exist'
            context = {'login_error': login_error}
            return render(request, 'loginsys/login.html', context)
    else:
        return render(request, 'loginsys/login.html', context)



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    register_form = UserCreationForm()
    context = {'register_form': register_form}
    if request.method == 'POST':
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password2'])

            auth.login(request, new_user)
            return HttpResponseRedirect('/')
        else:
            register_form = new_user_form
            context = {'register_form': register_form}
    return render(request, 'loginsys/register.html', context)

