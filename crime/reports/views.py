from django.shortcuts import render
from django.http import HttpResponse
from reports.models import Building, Location, CrimeReport

def home(request):
    buildings = Building.objects.order_by('name').distinct()
    return render(request, 'index.html', {'buildings': buildings})

def buildingdetail(request, slug):
    building = Building.objects.get(name_slug=slug)
    crimes = CrimeReport.objects.filter(building=building)
    return render(request, 'buildingdetail.html', {'building': building, 'crimes': crimes,})

