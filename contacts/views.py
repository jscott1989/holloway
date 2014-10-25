from django.shortcuts import render, redirect, get_object_or_404
from models import Contact, Group
from django.contrib import messages
from forms import ContactForm, GroupForm

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
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        # If we post then we will delete the user
        contact.delete()
        messages.success(request, "%s deleted" % contact.name)
        return redirect("contacts")
    return render(request, "contacts/confirm_delete.html", {"contact": contact})


def groups(request):
    """ Group list. """
    groups = Group.objects.all()
    return render(request, "contacts/groups/index.html", {"groups": groups})

def create_group(request):
    """ Create a new group. """
    group_form = GroupForm()
    if request.method == "POST":
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group = group_form.save()
            messages.success(request, "%s added" % group.name)
            return redirect("view_group", group.id)
    return render(request, "contacts/groups/create.html", {"form": group_form})

def view_group(request, pk):
    """ View a group. """
    group = get_object_or_404(Group, pk=pk)
    return render(request, "contacts/groups/view.html", {"group": group})

def edit_group(request, pk):
    """ Edit a group. """
    group = get_object_or_404(Group, pk=pk)
    group_form = GroupForm(instance=group)
    if request.method == "POST":
        group_form = GroupForm(request.POST, instance=group)
        if group_form.is_valid():
            group = group_form.save()
            messages.success(request, "%s updated" % group.name)
            return redirect("view_group", group.id)
    return render(request, "contacts/groups/edit.html", {"group": group, "form": group_form})

def delete_group(request, pk):
    """ Delete a group. """
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        # If we post then we will delete the group
        group.delete()
        messages.success(request, "%s deleted" % group.name)
        return redirect("groups")
    return render(request, "contacts/groups/confirm_delete.html", {"group": group})
