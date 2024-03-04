from rest_framework.viewsets import ModelViewSet
from ..models import Product
from .serializers import ProductSerializer


class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
