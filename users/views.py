from users.models import User
from rest_framework import viewsets
from users.serializers import UserSerializer
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer