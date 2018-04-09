
from rest_framework import serializers
from .models import Moonshot

class MoonshotSerializer(serializers.ModelSerializer):
  """Serializer to map the Model into JSON format"""

  class Meta:
    """Meta class to map serializer's fields with the models fields"""

    model = Moonshot
    fields = ('id', 'name', 'date_created', 'date_modified')
    read_only_fields = ('date_created', 'date_modified')
