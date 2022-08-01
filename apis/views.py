from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
# Create your views here.

from apis.models import (Incident, Individual, Organization)
from apis.serializers import (IncidentSerializer, IndividualSerializer, OrganizationSerializer)


class IncidentListCreateAPIView(APIView):

    def get(self, request):
        incidents = Incident.objects.filter(active=True)
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncidentDetailAPIView(APIView):

    def get_object(self, pk):
        incident = get_object_or_404(Incident, pk=pk)
        return incident

    def get(self, request, pk):
        incident = self.get_object(pk)
        serializer = IncidentSerializer(incident)
        return Response(serializer.data)

    def put(self, request, pk):
        incident = self.get_object(pk)
        serializer = IncidentSerializer(incident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        incident = self.get_object(pk)
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrganizationListCreateAPIView(APIView):

    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations,
                                            many=True,
                                            context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndividualListCreateAPIView(APIView):

    def get(self, request):
        individuals = Individual.objects.all()
        serializer = IndividualSerializer(individuals,
                                          many=True,
                                          context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = IndividualSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
