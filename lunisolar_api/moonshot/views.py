# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import MoonshotSerializer
from .models import Moonshot

class CreateView(generics.ListCreateAPIView):
  """This class defines the create behaviour of our rest api"""

  queryset = Moonshot.objects.all()
  serializer_class = MoonshotSerializer

  def perfrom_create(self, serializer):
    """Save the post data when creating a new Moonshot"""

    serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
  """This class defines the http GET, PUT and DELETE behaviour of our rest api"""
  
  queryset = Moonshot.objects.all()
  serializer_class = MoonshotSerializer
