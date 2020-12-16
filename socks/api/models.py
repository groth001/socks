from django.db import models
from django.utils import timezone

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)

class Role(models.Model):
    name = models.CharField(max_length=30)
    isrequired = models.BooleanField()

class Event(models.Model):
    name = models.CharField(max_length=30)
    starttime = models.DateTimeField(default=timezone.now) # maybe only need date
    endtime = models.DateTimeField(default=timezone.now)

class Employee(models.Model):
    NONE = 'None'
    TEAMLEAD = 'Team Lead'
    SUPERVISOR = 'Supervisor'

    RANKS = [
        (NONE, 'None'),
        (TEAMLEAD, 'Team Lead'),
        (SUPERVISOR, 'Supervisor'),
    ]

    NIGHT = 'Night'
    DAY = 'Day'
    SWING = "Swing"

    SHIFTS = [
        (NIGHT, 'Night'),
        (DAY, 'Day'),
        (SWING, 'Swing'),
    ]

    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rank = models.CharField(max_length=30, choices=RANKS, default=NONE)
    shift = models.CharField(max_length=30, choices=SHIFTS, default=NONE)
