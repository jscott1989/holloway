from django.shortcuts import render, redirect
from django.contrib.sites.models import Site
from forms import AdminForm
from django.contrib.auth.models import User

def require_no_users(func):
    """ Decorator to ensure that once a user is created, the wizard is disabled. """
    def inner(*args, **kwargs):
        if User.objects.count() > 0:
            return redirect('index')
        return func(*args, **kwargs)
    return inner

@require_no_users
def index(request):
    """ Introduce to holloway. """
    return render(request, "wizard/index.html")

@require_no_users
def site(request):
    """ Set up the site. """
    # TODO: Support a form to set this...

    try:
        site = Site.objects.get(pk=1)
    except:
        site = Site()
    
    site.id = 1
    site.name = "Holloway"
    site.domain = "http://localhost"
    site.save()

    return redirect('wizard_social')

    return render(request, "wizard/site.html")

@require_no_users
def social(request):
    """ Set up social auth. """
    # TODO: Allowing to setup auth options
    return redirect('wizard_admin')
    return render(request, "wizard/social.html")

@require_no_users
def admin(request):
    """ Set up default admin account. """
    admin_form = AdminForm()
    if request.method == "POST":
        admin_form = AdminForm(request.POST)
        if admin_form.is_valid():
            user = User.objects.create_user(admin_form.cleaned_data['username'], admin_form.cleaned_data['email_address'], admin_form.cleaned_data['password'])
            user.is_staff = True
            user.save()
            print user
            return redirect("index")
    return render(request, "wizard/admin.html", {"form": admin_form})
