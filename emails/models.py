from django.db import models
import jsonfield

class EmailTemplate(models.Model):
    owner = models.ForeignKey("auth.User")
    subject = models.CharField(max_length=100)
    html = models.TextField()
    text = models.TextField()
    required_fields = jsonfield.JSONField()
