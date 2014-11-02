from django.shortcuts import render, redirect, get_object_or_404
from models import EmailTemplate, SMTPAccount
from forms import EmailTemplateForm, EmailForm, AccountForm
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
    email_form = EmailForm(user=request.user)

    if request.method == "POST":
        email_form = EmailForm(request.POST,user=request.user)
        if email_form.is_valid():
            print email_form.cleaned_data['required_fields']
            from_account = email_form.cleaned_data['from_account']

            send_templated_email(request.user, email_form.contacts, from_account, email_form.cleaned_data['subject'], email_form.cleaned_data['html'], email_form.cleaned_data['text'])
            messages.success(request, "%s sent" % email_form.cleaned_data['subject'])
            # return redirect("index")
    return render(request, "emails/send.html", {"form": email_form})


@login_required
def accounts(request):
    """ Accounts list. """
    accounts = SMTPAccount.objects.filter(owner=request.user)
    return render(request, "accounts/index.html", {"accounts": accounts})

@login_required
def create_account(request):
    """ Create a new email account. """
    account_form = AccountForm()
    if request.method == "POST":
        account_form = AccountForm(request.POST)
        if account_form.is_valid():
            account = account_form.save(commit=False)
            account.owner = request.user
            account.save()
            messages.success(request, "%s added" % account.email_address)
            return redirect("view_account", account.id)
    return render(request, "accounts/create.html", {"form": account_form})

@login_required
def view_account(request, pk):
    """ View an email account. """
    account = get_object_or_404(SMTPAccount, pk=pk, owner=request.user)
    return render(request, "accounts/view.html", {"account": account})

@login_required
def edit_account(request, pk):
    """ Edit an email account. """
    account = get_object_or_404(SMTPAccount, pk=pk, owner=request.user)
    account_form = AccountForm(instance=account)
    if request.method == "POST":
        account_form = AccountForm(request.POST, instance=account)
        if account_form.is_valid():
            account = account_form.save()
            messages.success(request, "%s updated" % account.email_address)
            return redirect("view_account", account.id)
    return render(request, "accounts/edit.html", {"account": account, "form": account_form})

@login_required
def delete_account(request, pk):
    """ Delete an email account. """
    account = get_object_or_404(SMTPAccount, pk=pk, owner=request.user)
    if request.method == "POST":
        # If we post then we will delete the email account
        account.delete()
        messages.success(request, "%s deleted" % account.email_address)
        return redirect("accounts")
    return render(request, "accounts/confirm_delete.html", {"account": account})