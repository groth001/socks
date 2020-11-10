from rest_framework import serializers
from api.models import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name', 'region', 'team']

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['name']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']
