from typing import Protocol

from django.db import models

from rest_framework import permissions


class AuthoredModelProtocol(Protocol):
    author: models.Field


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow authors of an object to edit it.
    Assumes the model instance has an `author` attribute.
    """

    def has_object_permission(self, request, view, obj: AuthoredModelProtocol):
        # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `author`.
        return obj.author == request.user
