from django.db import models

#max_length of 50 for uncertain length

class CrimeReport(models.Model):
    incident_number = models.IntergerField()
    reported_time = models.CharField(max_length=16)
    status_code = models.CharField(max_length=50)
    occurred_time = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    incident_code = models.CharField(max_length=50)
    stolen = models.DecimalField()
    damaged = models.DecimalField()
    summary = models.CharField(max_length=256)
    
    
    

