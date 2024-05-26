# participants/models.py
from django.db import models
import uuid

class Participant(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, blank=True)
    points = models.IntegerField(default=0)
    qr_code_image = models.ImageField(upload_to='qr_codes/', blank=True)

