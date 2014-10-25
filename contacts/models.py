from django.db import models
import jsonfield

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    fields = jsonfield.JSONField()

    @property
    def name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def all_fields(self):
        """ A list of tuples - including the default data and custom fields """
        yield ("First Name", self.first_name)
        yield ("Last Name", self.last_name)
        yield ("Email", self.email)

        for i in self.fields.items():
            yield i
    

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contacts = models.ManyToManyField(Contact)
