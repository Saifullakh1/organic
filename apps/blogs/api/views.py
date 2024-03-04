from rest_framework.viewsets import ModelViewSet
from ..models import Blog
from .serializers import BlogSerializer


class BlogAPIViewSet(ModelViewSet):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializer

