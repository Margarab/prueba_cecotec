# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    ean = models.CharField(max_length=13, verbose_name=_('EAN'))
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=5, decimal_places=2)

    def __str__(self):
        return '{0} ({1}€)'.format(self.name, self.price)

    class Meta:
        ordering = ('name',)
