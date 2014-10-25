from django.shortcuts import render

def index(request):
    """ Site dashboard """
    return render(request, "index.html")
