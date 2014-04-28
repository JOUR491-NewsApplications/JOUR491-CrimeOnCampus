#!/usr/bin/env python
# encoding: utf-8

import sys, os

sys.setrecursionlimit(20000)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crime.settings") 

from reports.models import Building, Location, Incident, Status, CrimeReport

try:
    from BeautifulSoup import BeautifulSoup
except:
    from bs4 import BeautifulSoup
    
import urllib, urllib2, string, datetime, time, re
from django.template.defaultfilters import slugify, urlize

numbers = [2,3,4,5,6,7,8,9,10,11,12,13]


#html = urllib2.urlopen("https://scsapps.unl.edu/policereports/default.aspx")

for number in numbers:
    htmlfile = "html/%i.html" % number
    html = open(htmlfile, "rb")
    soup = BeautifulSoup(html)
    tables = soup.findAll('table')
    reports_container = tables[1] 
    rows = reports_container.findAll('tr')
    for row in rows:
        tds = row.findAll('td')
        reptid = int(row.find(id=re.compile('.*_IncidentNumberLabel')).string)
        reported = row.find(id=re.compile('.*_Label2')).string
        tickparse = time.strptime(reported, "%m/%d/%Y %H:%M")
        tick_date = datetime.datetime(tickparse.tm_year, tickparse.tm_mon, tickparse.tm_mday, tickparse.tm_hour, tickparse.tm_min)
        occurred = row.find(id=re.compile('.*_Label10')).string
        try:
            building = row.find(id=re.compile('.*_Label3')).string
        except:
            building = None
        street = row.find(id=re.compile('.*_Label4')).string
        incident = row.find(id=re.compile('.*_Label5')).string
        stoln = row.find(id=re.compile('.*_Label6')).string
        damage = row.find(id=re.compile('.*_Label7')).string
        clearance = row.find(id=re.compile('.*_Label8')).string
        narrative = row.find(id=re.compile('.*_Label9')).string
        if building == None:
            b = None
        else:
            try: 
                bslug = slugify(building)
                b = Building.objects.get(name_slug=bslug)
            except:
                bslug = slugify(building)
                b, bcreated = Building.objects.get_or_create(name=building, name_slug=bslug)
        if street == None:
            l = None
        else:
            addslug = slugify(street)
            l, lcreated = Location.objects.get_or_create(address=street, address_slug=addslug, building=b)
        if incident == None:
            i = None
        else:
            islug = slugify(incident)
            i, icreated = Incident.objects.get_or_create(name=incident, name_slug=islug)
        if clearance == None:
            s = None
        else:
            sslug = slugify(clearance)
            s, screated = Status.objects.get_or_create(name=clearance, name_slug=sslug)
        c, ccreated = CrimeReport.objects.get_or_create(incident_number=reptid, reported_time=tick_date, status_code=s, occurred_time=occurred, building=b, location=l, incident_code=i, stolen=stoln, damaged=damage, summary=narrative)
        print c
