from django.shortcuts import render

def index(request):
    """ Contacts list """
    return render(request, "contacts/index.html")

def groups(request):
    """ Groups list """
    return render(request, "contacts/groups.html")