# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name=_('ID'), editable=False)
    client_name = models.CharField(max_length=128, verbose_name=_('Client name'))
    client_surname = models.CharField(max_length=128, verbose_name=_('Client surname'))
    client_email = models.EmailField(max_length=128, verbose_name=_('Client email'))
    timestamp = models.DateTimeField(auto_now_add=True)



class Item(models.Model):

