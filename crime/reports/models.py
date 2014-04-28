from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def get_absolute_url(self):
        return "/buildings/%s/" % self.name_slug
    def __unicode__(self):
        return self.name

class Location(models.Model):
    address = models.CharField(max_length=255)
    address_slug = models.SlugField()
    city = models.CharField(max_length=255, default="Lincoln, NE")
    building = models.ForeignKey(Building, blank=True, null=True)
    def get_absolute_url(self):
        return "http://127.0.0.1:8000/buildings/%s/" % self.address_slug
    def __unicode__(self):
        return self.address

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
    status_code = models.ForeignKey(Status, blank=True, null=True)
    occurred_time = models.CharField(max_length=255, blank=True, null=True)
    building = models.ForeignKey(Building, blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    incident_code = models.ForeignKey(Incident, blank=True, null=True)
    stolen = models.CharField(max_length=255, blank=True, null=True)
    damaged = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    def get_absolute_url(self):
        return "/incident/%i/" % self.incident_number
    def __unicode__(self):
        return "A %s on %s" % (self.incident_code.name, self.reported_time)
