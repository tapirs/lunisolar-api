# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import MoonshotSerializer
from .serializers import UserSerializer
from .models import Moonshot
from rest_framework import permissions
from .permissions import IsOwner
from django.contrib.auth.models import User

class CreateView(generics.ListCreateAPIView):
  """This class defines the create behaviour of our rest api"""

  queryset = Moonshot.objects.all()
  serializer_class = MoonshotSerializer
  permission_classes = (permissions.IsAuthenticated, IsOwner)

  def perform_create(self, serializer):
    """Save the post data when creating a new Moonshot"""

    serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
  """This class defines the http GET, PUT and DELETE behaviour of our rest api"""
  
  queryset = Moonshot.objects.all()
  serializer_class = MoonshotSerializer
  permission_classes = (permissions.IsAuthenticated, IsOwner)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
