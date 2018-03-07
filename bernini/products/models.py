# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Product(models.Model):
    id = models.CharField(max_length=20, primary_key=True, verbose_name=_('ID'))
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=5, decimal_places=2)
