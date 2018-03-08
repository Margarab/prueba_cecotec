# -*- coding: utf-8 -*-
from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import uuid
from products import models as products_models
from django.contrib.auth import models as auth_models

class Order(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        verbose_name=_("Order number"),
        editable=False
    )
    client = models.ForeignKey(
        auth_models.User,
        verbose_name=_("Client"),
        related_name="orders",
        on_delete=models.PROTECT
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(
        products_models.Product,
        through='Item',
        through_fields=('order', 'product')
    )

    def __str__(self):
        return "{0} - {1}".format(self.id, self.client.username)

    class Meta:
        ordering = ('timestamp',)


class Item(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        products_models.Product,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[validators.MinValueValidator(1)]
    )
