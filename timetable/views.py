from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    count = User.objects.count()
    return render(request, 'timetable_home.html', {
        'count': count
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserCreationForm
    return render(request, 'registration/signup.html', {
        'form':form
    })

@login_required()
def secret_page(request):
    return render(request, 'registration/secret_page.html')