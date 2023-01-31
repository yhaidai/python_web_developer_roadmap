from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

from ..utils import AuthoredModelProtocol


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow authors of an object to edit it.

    Assumes the model instance has an `author` attribute.
    """

    def has_object_permission(self, request: Request, view: APIView, authored_object: AuthoredModelProtocol):
        # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `author`.
        return authored_object.author == request.user
