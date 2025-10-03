from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Petition
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    petitions = Petition.objects.all()
    return render(request, 'petitions/index.html', {'petitions': petitions})

@login_required
def create_petition(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Petition.objects.create(title=title, description=description, created_by=request.user)
        return redirect('petitions_index')
    return render(request, 'petitions/create.html')

@login_required
def vote_yes(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)
    petition.yes_votes.add(request.user)
    petition.no_votes.remove(request.user)
    return redirect('petitions_index')

@login_required
def vote_no(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)
    petition.no_votes.add(request.user)
    petition.yes_votes.remove(request.user)
    return redirect('petitions_index')
