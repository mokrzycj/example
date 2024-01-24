# views.py w aplikacji accounts

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Utworzenie użytkownika
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')  # Przekierowanie do strony głównej po zalogowaniu
            else:
                return HttpResponse('Konto jest nieaktywne.')
        else:
            return HttpResponse('Nieprawidłowe dane logowania.')
    else:
        return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
