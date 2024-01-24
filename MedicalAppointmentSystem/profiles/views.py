# views.py w aplikacji profiles

from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('some-view')  # Przekierowanie po utworzeniu profilu
    else:
        form = ProfileForm()
    return render(request, 'profiles/create_profile.html', {'form': form})

def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('some-view')  # Przekierowanie po edycji profilu
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})
