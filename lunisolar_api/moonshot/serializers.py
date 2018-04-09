
from rest_framework import serializers
from .models import Moonshot
from django.contrib.auth.models import User

class MoonshotSerializer(serializers.ModelSerializer):
  """Serializer to map the Model into JSON format"""

  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    """Meta class to map serializer's fields with the models fields"""

    model = Moonshot
    fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
    read_only_fields = ('date_created', 'date_modified')

class UserSerializer(serializers.ModelSerializer):
    moonshot = serializers.PrimaryKeyRelatedField(many=True, queryset=Moonshot.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'moonshot')
