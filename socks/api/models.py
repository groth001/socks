from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=30)

class Team(models.Model):
    name = models.CharField(max_length=30)

class Employee(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Shift(models.Model):
    name = models.CharField(max_length=30)

class Role(models.Model):
    name = models.CharField(max_length=30)
