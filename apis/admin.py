from django.contrib import admin
from apis.models import (Incident, Organization,Individual)
# Register your models here.

admin.site.register(Incident)
admin.site.register(Organization)
admin.site.register(Individual)
