from django.template import Template, Context

def send_templated_email(user, contacts, from_account, subject, html, text):
    """ Render the subject, html, and text templates for each contact and send the email. """

    for contact in contacts:
        r_subject = render_template(contact, subject)
        r_html = render_template(contact, html)
        r_text = render_template(contact, text)
        from_account.send_email(user, contact, r_subject, r_html, r_text)

def render_template(contact, template):
    """ Render a template with the fields from a contact. """
    fields = contact.all_fields

    template = Template(template)

    return template.render(Context(dict(fields)))