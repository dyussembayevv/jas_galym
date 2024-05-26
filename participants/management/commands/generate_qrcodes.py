# participants/management/commands/generate_qrcodes.py
from django.core.management.base import BaseCommand
from participants.models import Participant
import qrcode
import os
from django.conf import settings
from PIL import Image

class Command(BaseCommand):
    help = 'Generate unique QR codes for participants'

    def handle(self, *args, **kwargs):
        base_url = 'http://159.65.149.33/participant/'
        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'qr_codes')):
            os.makedirs(os.path.join(settings.MEDIA_ROOT, 'qr_codes'))

        for _ in range(1500):
            participant = Participant.objects.create()
            qr_data = f"{base_url}{participant.unique_id}"
            qr_img = qrcode.make(qr_data)

            qr_code_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes', f'{participant.unique_id}.png')
            qr_img.save(qr_code_path)

            # Update participant record with QR code path
            participant.qr_code_image = f'qr_codes/{participant.unique_id}.png'
            participant.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated QR codes'))

