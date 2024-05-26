# participants/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Participant

def participant_detail(request, unique_id):
    participant = get_object_or_404(Participant, unique_id=unique_id)
    if request.method == 'POST':
        participant.name = request.POST['name']
        participant.points = request.POST['points']
        participant.save()
        return redirect('participant_detail', unique_id=participant.unique_id)
    return render(request, 'participants/participant_detail.html', {'participant': participant})

