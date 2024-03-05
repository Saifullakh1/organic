from rest_framework.generics import CreateAPIView

from ..models import User
from .serializers import UserRegisterSerializer


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
