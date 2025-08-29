from rest_framework import routers
from .views import AluminiViewSet

# router = routers.SimpleRouter()
router=routers.DefaultRouter()
router.register(r'alumini', AluminiViewSet)
urlpatterns = router.urls

