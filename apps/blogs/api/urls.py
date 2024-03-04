from rest_framework import routers
from .views import BlogAPIViewSet


router = routers.DefaultRouter()
router.register(
    "blogs",
    BlogAPIViewSet
)

urlpatterns = router.urls
