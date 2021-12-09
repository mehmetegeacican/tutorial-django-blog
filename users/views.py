from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f'Account created for {username}, Your account has been created! You can now login')
            return redirect('signin')

    else:
        form = UserRegisterForm()
    return render(request, "users/sign_up.html",{'form': form})

@login_required
def profile(request):
    return render(request,"users/profile.html")



