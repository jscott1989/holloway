import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template import Template, Context

def send_templated_email(user, contacts, from_address, subject, html, text):
    """ Render the subject, html, and text templates for each contact and send the email. """
    for contact in contacts:
        r_subject = render_template(contact, subject)
        r_html = render_template(contact, html)
        r_text = render_template(contact, text)
        send_email(user, contact, from_address, r_subject, r_html, r_text)

def send_email(user, contact, from_address, subject, html, text):
    msg = MIMEMultipart("alternative")
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = contact.email

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    msg.attach(part1)
    msg.attach(part2)

    s = smtplib.SMTP("%s:%s" % (user.settings.smtp_host, user.settings.smtp_port))
    if user.settings.smtp_username:
        s.login(user.settings.smtp_username, user.settings.smtp_password)

    s.sendmail(from_address, contact.email, msg.as_string())
    s.quit()

def render_template(contact, template):
    """ Render a template with the fields from a contact. """
    fields = contact.all_fields

    template = Template(template)

    return template.render(Context(dict(fields)))