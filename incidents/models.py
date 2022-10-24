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
    time_creation = models.DateTimeField(default=timezone.now)
    cves = models.ManyToManyField("CommonVulnerabilityExposure", related_name="cve_incidents")
    targets = models.ManyToManyField("IncidentTarget", related_name="target_incidents")

    @property
    def cve_numbers(self):
        return [cve.cve_number for cve in self.cves.all()]

    @property
    def object(self):
        return [t.name for t in self.targets.all()]

    class Meta:
        db_table = "incidents"


class IncidentTarget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = "incident_targets"


class CommonVulnerabilityExposure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cve_number = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = "cves"
