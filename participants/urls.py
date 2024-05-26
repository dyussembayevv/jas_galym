# participants/urls.py
from django.urls import path
from .views import participant_detail

urlpatterns = [
    path('participant/<uuid:unique_id>/', participant_detail, name='participant_detail'),
]
