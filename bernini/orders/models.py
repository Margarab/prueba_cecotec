# -*- coding: utf-8 -*-
from django.db import models
from django.core import validators
from django.contrib.auth import models as auth_models
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import csv
import uuid
import decimal
import datetime
from io import StringIO
from products import models as products_models


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

    def get_csv(self):
        csvfile = StringIO()
        writer = csv.writer(csvfile)
        for item in self.items.all():
            writer.writerow([self.id, item.product.name, item.product.ean, item.quantity, self.client.username, datetime.datetime.strftime(self.timestamp, '%y-%m-%d %H:%M')])
        return csvfile.getvalue()

    def send_email(self):
        email_msg = EmailMultiAlternatives(
            "New order",
            render_to_string('order_email.txt', {'order': self}),
            settings.DEFAULT_FROM_EMAIL,
            [settings.ORDERS_EMAIL]
        )
        email_msg.attach_alternative(render_to_string('order_email.html', {'order': self}), "text/html")
        email_msg.attach('order_{0}.csv'.format(self.id), self.get_csv(), "text/csv")
        email_msg.send(fail_silently=False)


    @property
    def get_total_price(self):
        return sum(i.get_total_price for i in self.items.all())

    def __str__(self):
        return "{0} - {1} Total: {2}€".format(self.id, self.client.username, self.get_total_price)

    class Meta:
        ordering = ('-timestamp',)


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

    @property
    def get_total_price(self):
        return decimal.Decimal(self.quantity) * self.product.price

    def __str__(self):
        return "{0} - {1} x{2} Total:{3}€".format(self.order.id, self.product.name, self.quantity, self.get_total_price)
