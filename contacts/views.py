from django.shortcuts import render, redirect, get_object_or_404
from models import Contact
from django.contrib import messages
from forms import ContactForm

def index(request):
    """ Contacts list. """
    contacts = Contact.objects.all()
    return render(request, "contacts/index.html", {"contacts": contacts})

def create_contact(request):
    """ Create a new contact. """
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            messages.success(request, "%s added" % contact.name)
            return redirect("view_contact", contact.id)
    return render(request, "contacts/create.html", {"form": contact_form})

def view_contact(request, pk):
    """ View a contact. """
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contacts/view.html", {"contact": contact})

def edit_contact(request, pk):
    """ Edit a contact. """
    contact = get_object_or_404(Contact, pk=pk)
    contact_form = ContactForm(instance=contact)
    if request.method == "POST":
        contact_form = ContactForm(request.POST, instance=contact)
        if contact_form.is_valid():
            contact = contact_form.save()
            messages.success(request, "%s updated" % contact.name)
            return redirect("view_contact", contact.id)
    return render(request, "contacts/edit.html", {"contact": contact, "form": contact_form})

def delete_contact(request, pk):
    """ Delete a contact. """
    # TODO: If we use this "confirm" functionality again,
    # abstract it into a decorator
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        # If we post then we will delete the user
        contact.delete()
        messages.success(request, "%s deleted" % contact.name)
        return redirect("contacts")
    return render(request, "contacts/confirm_delete_contact.html", {"contact": contact})


def groups(request):
    """ Groups list. """
    return render(request, "contacts/groups.html")