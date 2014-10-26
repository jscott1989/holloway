from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    """ Site dashboard """
    # First check if there are 0 users, if so we forward to the wizard
    
    if User.objects.count() == 0:
        return redirect('wizard')
    elif not request.user.is_authenticated():
        return redirect('account_login')

    return render(request, "index.html")
