from rest_framework import routers
from .api import ProjectViewSet

# Set URL routers
router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projectregistry')

urlpatterns = router.urls
