"""
Base models used by the entities that model the application's domain.
"""
from tortoise import fields
from tortoise.models import Model


class BaseEntityMixin(Model):
    """
    Base mixin to be used with multiple inheritance when composing concrete entities.
    """

    id = fields.UUIDField(pk=True)

    created_at = fields.DatetimeField(null=True, auto_now_add=True, index=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True, index=True)

    class Meta:
        abstract = True
