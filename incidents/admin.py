from django.contrib import admin

from incidents.models import Incident, IncidentTarget, CommonVulnerabilityExposure


class IncidentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Incident, IncidentAdmin)


class IncidentTargetAdmin(admin.ModelAdmin):
    pass


admin.site.register(IncidentTarget, IncidentTargetAdmin)


class CommonVulnerabilityExposureAdmin(admin.ModelAdmin):
    pass


admin.site.register(CommonVulnerabilityExposure, CommonVulnerabilityExposureAdmin)
