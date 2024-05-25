from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers.user_serializer import RegistrationSerializer

User = get_user_model()


@extend_schema_view(post=extend_schema(summary='Реєстрація користувача', tags=['Аутентифікація та авторизація']))
class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
