from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def get_absolute_url(self):
        return "/buildings/%s/" % self.name_slug
    def __unicode__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def get_absolute_url(self):
        return "/locations/%s/" % self.name_slug
    def __unicode__(self):
        return self.name

class Incident(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def get_absolute_url(self):
        return "/type/%s/" % self.name_slug
    def __unicode__(self):
        return self.name
    
class Status(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def get_absolute_url(self):
        return "/status/%s/" % self.name_slug
    def __unicode__(self):
        return self.name

class CrimeReport(models.Model):
    incident_number = models.IntegerField()
    reported_time = models.DateTimeField()
    status_code = models.ForeignKey(Status)
    occurred_time = models.CharField(max_length=255)
    building = models.ForeignKey(Building, blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    incident_code = models.ForeignKey(Incident, blank=True, null=True)
    stolen = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=15)
    damaged = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=15)
    summary = models.CharField(max_length=256, blank=True, null=True)
    def get_absolute_url(self):
        return "/incident/%i/" % self.incident_number
    def __unicode__(self):
        return self.incident_number
