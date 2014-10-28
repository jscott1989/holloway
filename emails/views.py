from django.shortcuts import render, redirect, get_object_or_404
from models import EmailTemplate
from forms import EmailTemplateForm, EmailForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from emails import send_templated_email

@login_required
def email_templates(request):
    """ Email Templates list. """
    email_templates = EmailTemplate.objects.filter(owner=request.user)
    return render(request, "email_templates/index.html", {"email_templates": email_templates})

@login_required
def create_email_template(request):
    """ Create a new email template. """
    email_template_form = EmailTemplateForm()
    if request.method == "POST":
        email_template_form = EmailTemplateForm(request.POST)
        if email_template_form.is_valid():
            email_template = email_template_form.save(commit=False)
            email_template.owner = request.user
            email_template.save()
            messages.success(request, "%s added" % email_template.subject)
            return redirect("view_email_template", email_template.id)
    return render(request, "email_templates/create.html", {"form": email_template_form})

@login_required
def view_email_template(request, pk):
    """ View an email template. """
    email_template = get_object_or_404(EmailTemplate, pk=pk, owner=request.user)
    return render(request, "email_templates/view.html", {"email_template": email_template})

@login_required
def edit_email_template(request, pk):
    """ Edit an email template. """
    email_template = get_object_or_404(EmailTemplate, pk=pk, owner=request.user)
    email_template_form = EmailTemplateForm(instance=email_template)
    if request.method == "POST":
        email_template_form = EmailTemplateForm(request.POST, instance=email_template)
        if email_template_form.is_valid():
            email_template = email_template_form.save()
            messages.success(request, "%s updated" % email_template.subject)
            return redirect("view_email_template", email_template.id)
    return render(request, "email_templates/edit.html", {"email_template": email_template, "form": email_template_form})

@login_required
def delete_email_template(request, pk):
    """ Delete an email template. """
    email_template = get_object_or_404(EmailTemplate, pk=pk, owner=request.user)
    if request.method == "POST":
        # If we post then we will delete the email template
        email_template.delete()
        messages.success(request, "%s deleted" % email_template.subject)
        return redirect("email_templates")
    return render(request, "email_templates/confirm_delete.html", {"email_template": email_template})

@login_required
def send_email(request):
    """ Send a new email. """
    email_form = EmailForm()
    if request.method == "POST":
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            send_templated_email(request.user, email_form.contacts, email_form.cleaned_data['from_address'], email_form.cleaned_data['subject'], email_form.cleaned_data['html'], email_form.cleaned_data['text'])
            messages.success(request, "%s sent" % email_form.cleaned_data['subject'])
            # return redirect("index")
    return render(request, "emails/send.html", {"form": email_form})
