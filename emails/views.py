from django.shortcuts import render

def index(request):
    """ Email template list """
    return render(request, "emails/index.html")