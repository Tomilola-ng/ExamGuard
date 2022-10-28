from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from users.forms import CustomUserCreationForm



# Create your views here.
@login_required
def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == 'GET':
        context = {
            'form': CustomUserCreationForm
        }
        return render(request, 'users/register.html', context )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))
    
    context = {
        'form': CustomUserCreationForm,
        'msg': 'Use a different email or different username'
    }
    return render(request, 'users/register.html', context )




