from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from apis.models import (Incident, Organization, Individual)

class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incident
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = "__all__"


class IndividualSerializer(serializers.ModelSerializer):

    class Meta:
        model = Individual
        fields = "__all__"

