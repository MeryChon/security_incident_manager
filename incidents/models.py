import enum
import uuid

from django.db import models
from django.utils import timezone


class IncidentType(enum.Enum):
    bruteforce = "Bruteforce Attack"


class Incident(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, choices=[(t.name, t.value) for t in IncidentType])
    description = models.TextField(blank=True)
    object = models.ForeignKey("IncidentTarget", on_delete=models.PROTECT, help_text="Target of the attack")
    time_creation = models.DateTimeField(default=timezone.now)

    @property
    def cve_numbers(self):
        return [cve.cve_number for cve in self.cve_objects]

    class Meta:
        db_table = "incidents"


class IncidentTarget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = "incident_targets"


class CommonVulnerabilityExposure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cve_number = models.CharField(max_length=64)
    cna_reference = models.CharField(max_length=256)
    incidents = models.ManyToManyField(Incident, related_name="cve_objects", blank=True, db_table="incident_cves")

    class Meta:
        db_table = "cves"
