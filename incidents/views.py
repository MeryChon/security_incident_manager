from rest_framework.viewsets import ModelViewSet

from incidents.models import Incident
from incidents.serializers import IncidentSerializer


class IncidentViewSet(ModelViewSet):
    serializer_class = IncidentSerializer
    queryset = Incident.objects

    # def get_queryset(self):
    #     return Incident.objects
