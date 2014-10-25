from django.db import models
import jsonfield

class EmailTemplate(models.Model):
    subject = models.CharField(max_length=100)
    html = models.TextField()
    text = models.TextField()
    required_fields = jsonfield.JSONField()
