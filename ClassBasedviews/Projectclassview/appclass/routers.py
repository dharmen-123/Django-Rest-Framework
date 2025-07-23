from rest_framework import routers
from .views import StudentViewSet

router = routers.SimpleRouter()
router.register(r'students', StudentViewSet)
urlpatterns = router.urls