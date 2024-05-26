import os
from django.core.management.base import BaseCommand
from django.conf import settings
from participants.models import Participant

class Command(BaseCommand):
    help = 'Delete all participants and their QR codes'

    def handle(self, *args, **kwargs):
        participants = Participant.objects.all()

        # Delete QR code images from the file system
        for participant in participants:
            if participant.qr_code_image:
                qr_code_path = os.path.join(settings.MEDIA_ROOT, participant.qr_code_image.name)
                if os.path.exists(qr_code_path):
                    os.remove(qr_code_path)

        # Delete Participant instances from the database
        participants.delete()

        self.stdout.write(self.style.SUCCESS('Successfully deleted all participants and their QR codes'))
