from django.db import models
from datetime import date

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)

class Shiftevent(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30, default='Other')
    date = models.DateField(default=date.today)

class Oooevent(models.Model):
    date = models.DateField(default=date.today)
    name = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    reason = models.CharField(max_length=30);

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
