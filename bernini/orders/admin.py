from django.contrib import admin
from .models import Order

class ProductInline(admin.TabularInline):
    model = Order.products.through

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'client')
    exclude = ['client',]
    inlines = [
        ProductInline,
    ]

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.client = request.user
        obj.save()

