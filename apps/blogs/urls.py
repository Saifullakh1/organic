from django.urls import path
from .views import detail


urlpatterns = [
    path('blog/<int:id>', detail, name='blog-detail')
]
