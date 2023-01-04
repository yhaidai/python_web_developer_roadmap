from typing import Protocol

from django.db import models


class AuthoredModelProtocol(Protocol):
    author: models.Field
