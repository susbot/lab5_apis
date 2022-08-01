from django.urls import path
from apis.views import (IncidentListCreateAPIView,
                        IncidentDetailAPIView,
                        IndividualListCreateAPIView,
                        OrganizationListCreateAPIView)

urlpatterns = [
    path("incident/", IncidentListCreateAPIView.as_view(), name="incident-list"),
    path("incident/<int:pk>/", IncidentDetailAPIView.as_view(), name="incident-detail"),
    path("individual/", IndividualListCreateAPIView.as_view(), name="individual-list"),
    path("organization", OrganizationListCreateAPIView.as_view(), name="organization-list"),
]