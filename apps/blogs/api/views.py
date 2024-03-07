from rest_framework.viewsets import ModelViewSet
from ..models import Blog
from .serializers import BlogSerializer
from rest_framework import permissions, status
from rest_framework.response import Response


class BlogAPIViewSet(ModelViewSet):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        user = request.user
        blogs = Blog.objects.filter(user=user)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



