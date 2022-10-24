from rest_framework import serializers

from incidents.models import Incident, IncidentTarget, CommonVulnerabilityExposure


class CommonVulnerabilityExposureListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        pass

    # def to_representation(self, data):
    #     return [inst.cve_number for inst in data]


class CommonVulnerabilityExposureSerializer(serializers.ModelSerializer):
    cve_number = serializers.CharField(max_length=64)

    class Meta:
        model = CommonVulnerabilityExposure
        list_serializer_class = CommonVulnerabilityExposureListSerializer
        fields = (
            'cve_number',
        )


class IncidentTargetListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        pass

    # def to_representation(self, data):
    #     return [inst.name for inst in data]


class IncidentTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentTarget
        list_serializer_class = IncidentTargetListSerializer
        fields = ("name",)


class IncidentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_blank=False, allow_null=False, max_length=128)
    description = serializers.CharField(allow_blank=True)
    # cve_numbers = CommonVulnerabilityExposureSerializer(many=True)
    # object = IncidentTargetSerializer(many=True)

    class Meta:
        model = Incident
        fields = (
            "id",
            "name",
            "description",
            "time_creation",
            "cve_numbers",
            "object"
        )
