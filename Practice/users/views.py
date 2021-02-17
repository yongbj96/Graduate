from rest_framework import viewsets
from users.serializers import UserSerializer
from users.models import User

# Django-restframework JOIN 기능
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer