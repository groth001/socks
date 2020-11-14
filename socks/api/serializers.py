from rest_framework import serializers
from api.models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name', 'isrequired']
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'starttime', 'endtime']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'password', 'team', 'rank', 'shift']
