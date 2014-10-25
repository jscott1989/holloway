from django.shortcuts import render, redirect, get_object_or_404
from models import EmailTemplate
from forms import EmailTemplateForm
from django.contrib import messages

def email_templates(request):
    """ Email Templates list. """
    email_templates = EmailTemplate.objects.all()
    return render(request, "email_templates/index.html", {"email_templates": email_templates})

def create_email_template(request):
    """ Create a new email template. """
    email_template_form = EmailTemplateForm()
    if request.method == "POST":
        email_template_form = EmailTemplateForm(request.POST)
        if email_template_form.is_valid():
            email_template = email_template_form.save()
            messages.success(request, "%s added" % email_template.subject)
            return redirect("view_email_template", email_template.id)
    return render(request, "email_templates/create.html", {"form": email_template_form})

def view_email_template(request, pk):
    """ View an email template. """
    email_template = get_object_or_404(EmailTemplate, pk=pk)
    return render(request, "email_templates/view.html", {"email_template": email_template})

def edit_email_template(request, pk):
    """ Edit an email template. """
    email_template = get_object_or_404(EmailTemplate, pk=pk)
    email_template_form = EmailTemplateForm(instance=email_template)
    if request.method == "POST":
        email_template_form = EmailTemplateForm(request.POST, instance=email_template)
        if email_template_form.is_valid():
            email_template = email_template_form.save()
            messages.success(request, "%s updated" % email_template.subject)
            return redirect("view_email_template", email_template.id)
    return render(request, "email_templates/edit.html", {"email_template": email_template, "form": email_template_form})

def delete_email_template(request, pk):
    """ Delete an email template. """
    email_template = get_object_or_404(EmailTemplate, pk=pk)
    if request.method == "POST":
        # If we post then we will delete the email template
        email_template.delete()
        messages.success(request, "%s deleted" % email_template.subject)
        return redirect("email_templates")
    return render(request, "email_templates/confirm_delete.html", {"email_template": email_template})
