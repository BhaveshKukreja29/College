from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()

    users = User.objects.all()
    return render(request, 'home.html', {'form': form, 'users': users})

