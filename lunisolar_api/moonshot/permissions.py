from rest_framework.permissions import BasePermission
from .models import Moonshot

class IsOwner(BasePermission):
  """Custom permission class to allow only moonshot owners to edit them"""

  def has_object_permission(self, request, view, obj):
    """Return true if permission is granted to moonshot owner"""

    if isinstance(obj, Moonshot):
      return obj.owner == request.user
    return obj.owner == request.user
