from django.contrib.auth.models import User, Group
from quickstart.serializers import GroupSerializers, UserSerializer
from rest_framework import permissions, viewsets

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    Permision_class = [permissions.IsAuthenticated]


class GroupViewSets(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializers
    permision_class = [permissions.IsAuthenticated]