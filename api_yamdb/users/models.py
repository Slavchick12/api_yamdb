from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_ROLES = (
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(
        _('email address'),
        max_length=254,
        unique=True,
    )
    bio = models.TextField(_('biography'), blank=True)
    role = models.CharField(
        _('custom roles'),
        max_length=16,
        choices=USER_ROLES,
        default='user'
    )

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'username'],
                name='unique_email_username'
            )
        ]

        ordering = ['pk']
