from rest_framework import routers
from .views import StudentViewSet

# router = routers.SimpleRouter()
router=routers.DefaultRouter()
router.register(r'students', StudentViewSet)
urlpatterns = router.urls

