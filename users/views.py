from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.shortcuts import render, get_object_or_404, redirect

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:feed')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
    return render(request, 'users/profile.html', {'form': form})

@login_required
def user_profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    is_following = profile_user in request.user.following.all()

    return render(request, 'users/user_profile.html', {
        'profile_user': profile_user,
        'is_following': is_following
    })