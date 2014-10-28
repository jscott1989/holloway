from django.core.management.base import BaseCommand, CommandError
import keyczar
from keyczar import keyczart
import os
import os.path

class Command(BaseCommand):
    help = "Generate encryption keys, if they don't already exist"

    def handle(self, *args, **options):
        if os.path.exists("keyset"):
            print "Keys already generated."
            return
        print "Generating keys"
        os.mkdir("keyset")
        keyczart.main(['create','--location=keyset','--purpose=crypt'])
        keyczart.main(['addkey','--location=keyset' ,'--status=primary'])
        print "Done"