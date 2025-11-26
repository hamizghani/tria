from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Akun kamu berhasil dibuat! Selamat datang di Tria.')
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Selamat datang kembali, {user.username}!')
            
            # Redirect to next parameter or home
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Username atau password salah.')
    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, 'Kamu berhasil logout. Sampai jumpa lagi!')
    return redirect('home')


@login_required
def profile(request):
    """Simple profile page showing user info and a logout action."""
    context = {
        'user': request.user,
    }
    return render(request, 'profile.html', context)