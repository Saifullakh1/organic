from rest_framework import routers
from .views import ProductAPIViewSet


router = routers.DefaultRouter()
router.register(
    prefix="products",
    viewset=ProductAPIViewSet,
)

urlpatterns = router.urls
