from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Petition, Vote

@login_required
def index(request):
    petitions = Petition.objects.all()
    for petition in petitions:
        petition.has_voted = petition.votes.filter(user=request.user).exists()

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
def delete_petition(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)

    if petition.created_by == request.user:
        petition.delete()
    return redirect('petitions_index') 

@login_required
def vote_yes(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)
    if Vote.objects.filter(petition=petition, user=request.user).exists():
        return redirect('petitions_index')  # Redirect if the user has already voted

    # Create or update vote
    Vote.objects.create(
        petition=petition,
        user=request.user,
        vote_type='yes'
    )
    return redirect('petitions_index')

@login_required
def vote_no(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)
    if Vote.objects.filter(petition=petition, user=request.user).exists():
        return redirect('petitions_index')  # Redirect if the user has already voted

    # Create or update vote
    Vote.objects.create(
        petition=petition,
        user=request.user,
        vote_type='no'
    )
    return redirect('petitions_index')