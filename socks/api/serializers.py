from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

#class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ['id', 'username', 'password', 'email']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']

class ShifteventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shiftevent
        fields = ['name', 'role', 'date']

class OooeventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oooevent
        fields = ['date', 'name', 'team', 'reason']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'team', 'rank', 'shift']
