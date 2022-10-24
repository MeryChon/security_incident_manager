from rest_framework import routers

from incidents.views import IncidentViewSet

router = routers.DefaultRouter()

router.register(r'', IncidentViewSet, basename='incidents')

urlpatterns = router.urls
