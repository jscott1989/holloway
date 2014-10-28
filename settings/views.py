from django.shortcuts import render, redirect
from models import Settings
from forms import SettingsForm
from django.contrib import messages

def index(request):
    settings = request.user.settings

    settings_form = SettingsForm(instance=settings)
    if request.method == "POST":
        settings_form = SettingsForm(request.POST, instance=settings)
        if settings_form.is_valid():
            settings = settings_form.save(commit=False)
            settings.owner = request.user
            settings.save()
            messages.success(request, "Settings updates")
            return redirect("settings")

    return render(request, "settings/index.html", {"form": settings_form})
