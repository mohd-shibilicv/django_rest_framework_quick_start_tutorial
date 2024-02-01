from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets

from .serializers import UserSerializers, GroupSerializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [permissions.IsAuthenticated]
