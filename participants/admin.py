from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'name', 'points', 'qr_code_image')
    search_fields = ('name', 'unique_id')
