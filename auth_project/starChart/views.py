from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import starSightingForm
from .models import starSighting

@login_required
def star(request):
    if request.method == 'POST':
        form = starSightingForm(request.POST)
        if form.is_valid():
            star_sighting = form.save(commit=False)
            star_sighting.user = request.user
            star_sighting.save()
            return redirect('star')
    else:
        form = starSightingForm()
    return render(request, 'star.html', {'form': form})

@login_required
def star(request):
    sightings = starSighting.objects.filter(user=request.user).order_by('-date_seen')
    return render(request, 'star.html', {'sightings': sightings})