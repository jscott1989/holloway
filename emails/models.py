import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.db import models
from encrypted_fields import EncryptedCharField, EncryptedEmailField
import jsonfield

class EmailTemplate(models.Model):
    owner = models.ForeignKey("auth.User")
    subject = models.CharField(max_length=100)
    html = models.TextField()
    text = models.TextField()
    required_fields = jsonfield.JSONField()

class Account(models.Model):
    """ An account for sending emails. """
    owner = models.ForeignKey("auth.User", related_name="accounts")
    email_address = EncryptedEmailField()

    def __unicode__(self):
        return self.email_address

    def send_email(self, user, contact, subject, html, text):
        if self.smtpaccount:
            self.smtpaccount.send_email(user, contact,subject, html, text)
        # TODO This is ugly... there must be a nicer way

class SMTPAccount(Account):
    """ An account for sending emails via SMTP. """
    smtp_host = EncryptedCharField(max_length=100, null=True)
    smtp_port = models.IntegerField(null=True)
    smtp_username = EncryptedCharField(max_length=100, null=True)
    smtp_password = EncryptedCharField(max_length=100, null=True)

    def send_email(self, user, contact, subject, html, text):
        msg = MIMEMultipart("alternative")
        msg['Subject'] = subject
        msg['From'] = self.email_address
        msg['To'] = contact.email

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        msg.attach(part1)
        msg.attach(part2)

        s = smtplib.SMTP("%s:%s" % (self.smtp_host, self.smtp_port))
        if self.smtp_username:
            s.login(self.smtp_username, self.smtp_password)

        s.sendmail(self.email_address, contact.email, msg.as_string())
        s.quit()