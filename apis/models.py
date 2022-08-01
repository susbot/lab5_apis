from django.db import models


# Create your models here.

incident_type = (
    ("Inadvertent Data Exposure", "Inadvertent Data Exposure"),
    ("Security Misconfiguration", "Security Misconfiguration"),
    ("Product Vulnerability", "Product Vulnerability"),
    ("Vendor Incident", "Vendor Incident"),
)

severity = (
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
    ("Critical", "Critical"),
)

class Organization(models.Model):
    name = models.CharField(max_length=60)
    street_address = models.CharField(max_length=60)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=10)
    zipcode = models.IntegerField()
    email = models.EmailField(max_length=50, null=False)

    def __str__(self):
        return f"{self.name}"


class Individual(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=50, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Incident(models.Model):
    entity = models.ForeignKey(Organization,
                               on_delete=models.CASCADE,
                               related_name="organization")
    author = models.ForeignKey(Individual,
                               on_delete=models.CASCADE,
                               related_name="individual")
    type = models.CharField(max_length=40, choices=incident_type)
    title = models.CharField(max_length=120)
    situation = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    notes = models.TextField()
    active = models.BooleanField(default=True)
    level = models.CharField(max_length=20, choices=severity)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.entity} {self.author}"
