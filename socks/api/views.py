#from django.shortcuts import render
from api.models import *
from api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class RegionList(APIView):
    """
    List all Regions, or create a new Region
    """
    def get(self, request, format=None):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegionDetail(APIView):
    """
    Retrieve, update or delete a Region.
    """
    def get_object(self, pk):
        try:
           return Region.objects.get(pk=pk)
       except Region.DoesNotExist:
           raise Http404

    def get(self, request, pk, format=None):
        region = self.get_object(pk)
        serializer = RegionSerializer(region)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        region = self.get_object(pk)
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        region = self.get_object(pk)
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeamList(APIView):
    """
    List all Teams, or create a new Team.
    """
    def get(self, request, format=None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDetail(APIView):
    """
    Retrieve, update or delete a Team.
    """
    def get_object(self, pk):
       try:
           return Team.objects.get(pk=pk)
       except Team.DoesNotExist:
           raise Http404

    def get(self, request, pk, format=None):
        team = self.get_object(pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        team = self.get_object(pk)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        team = self.get_object(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
