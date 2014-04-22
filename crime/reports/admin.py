from django.contrib import admin
from reports.models import Building, Location, Incident, Status, CrimeReport

admin.site.register(Building)
admin.site.register(Location)
admin.site.register(Incident)
admin.site.register(Status)
admin.site.register(CrimeReport)
