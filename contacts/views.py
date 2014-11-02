from django.shortcuts import render, redirect, get_object_or_404
from models import Contact, Group
from django.contrib import messages
from forms import ContactForm, GroupForm, ImportUploadForm
from django.contrib.auth.decorators import login_required
import csv

@login_required
def index(request):
    """ Contacts list. """
    contacts = Contact.objects.filter(owner=request.user)
    return render(request, "contacts/index.html", {"contacts": contacts})

@login_required
def create_contact(request):
    """ Create a new contact. """
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, "%s added" % contact.name)
            return redirect("view_contact", contact.id)
    return render(request, "contacts/create.html", {"form": contact_form})

@login_required
def view_contact(request, pk):
    """ View a contact. """
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    return render(request, "contacts/view.html", {"contact": contact})

@login_required
def edit_contact(request, pk):
    """ Edit a contact. """
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    contact_form = ContactForm(instance=contact)
    if request.method == "POST":
        contact_form = ContactForm(request.POST, instance=contact)
        if contact_form.is_valid():
            contact = contact_form.save()
            messages.success(request, "%s updated" % contact.name)
            return redirect("view_contact", contact.id)
    return render(request, "contacts/edit.html", {"contact": contact, "form": contact_form})

@login_required
def delete_contact(request, pk):
    """ Delete a contact. """
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    if request.method == "POST":
        # If we post then we will delete the user
        contact.delete()
        messages.success(request, "%s deleted" % contact.name)
        return redirect("contacts")
    return render(request, "contacts/confirm_delete.html", {"contact": contact})

@login_required
def groups(request):
    """ Group list. """
    groups = Group.objects.filter(owner=request.user)
    return render(request, "contacts/groups/index.html", {"groups": groups})

@login_required
def create_group(request):
    """ Create a new group. """
    group_form = GroupForm()
    if request.method == "POST":
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group = group_form.save(commit=False)
            group.owner = request.user
            group.save()
            messages.success(request, "%s added" % group.name)
            return redirect("view_group", group.id)
    return render(request, "contacts/groups/create.html", {"form": group_form})

@login_required
def view_group(request, pk):
    """ View a group. """
    group = get_object_or_404(Group, pk=pk, owner=request.user)
    return render(request, "contacts/groups/view.html", {"group": group})

@login_required
def edit_group(request, pk):
    """ Edit a group. """
    group = get_object_or_404(Group, pk=pk, owner=request.user)
    group_form = GroupForm(instance=group)
    if request.method == "POST":
        group_form = GroupForm(request.POST, instance=group)
        if group_form.is_valid():
            group = group_form.save()
            messages.success(request, "%s updated" % group.name)
            return redirect("view_group", group.id)
    return render(request, "contacts/groups/edit.html", {"group": group, "form": group_form})

@login_required
def delete_group(request, pk):
    """ Delete a group. """
    group = get_object_or_404(Group, pk=pk, owner=request.user)
    if request.method == "POST":
        # If we post then we will delete the group
        group.delete()
        messages.success(request, "%s deleted" % group.name)
        return redirect("groups")
    return render(request, "contacts/groups/confirm_delete.html", {"group": group})

@login_required
def import_contacts(request):
    """ Import contacts from CSV. """
    import_upload_form = ImportUploadForm()
    errors = []
    if request.method == "POST":
        import_upload_form = ImportUploadForm(request.POST, request.FILES)
        if import_upload_form.is_valid():
            data = csv.DictReader(request.FILES['file'].read().splitlines())
            datalist = []
            for i, row in enumerate(data):
                datalist.append(row)
                for r in Contact.REQUIRED_FIELDS:
                    if row.get(r, "").strip() == "":
                        errors.append("Error on line " + str(i + 1) + ": missing required field " + r)

            if len(errors) == 0:
                request.session['imported_contacts'] = datalist
                return redirect("import_contacts_confirm")

    return render(request, "contacts/import/upload.html", {"form": import_upload_form, "errors": errors})

@login_required
def import_contacts_confirm(request):
    """ Confirm import of contacts from CSV. """
    if request.method == "POST":
        for contact_info in request.session['imported_contacts']:
            contact, created = Contact.objects.get_or_create(email=contact_info['email'], owner=request.user)

            for attr in Contact.REQUIRED_FIELDS:
                setattr(contact, attr, contact_info[attr])

            fields = contact.fields
            for attr in [c for c in contact_info.keys() if not c in Contact.REQUIRED_FIELDS]:
                contact.fields[attr] = contact_info[attr]

            contact.save()

        messages.success(request, "%s contacts imported" % len(request.session['imported_contacts']))
        del request.session['imported_contacts']
        return redirect("contacts")

    contacts = request.session['imported_contacts']
    keys = set(reduce(lambda x, y: x + y, [c.keys() for c in contacts]))

    keys = sorted(keys, key=lambda x : 1 if x == "email" else 2 if x == "first_name" else 3 if x == "last_name" else 4)

    return render(request, "contacts/import/confirm.html", {"keys": keys, "contacts": contacts})