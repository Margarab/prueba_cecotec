from django.contrib import admin
from .models import Order


class ProductInline(admin.TabularInline):
    model = Order.products.through

class MyAdminSite(admin.AdminSite):
    site_header = 'Zapatos Bernini'
    site_title = 'Orders'
    index_title = 'Manage orders'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'client')
    exclude = ['client',]
    inlines = [
        ProductInline,
    ]

    def queryset(self, request):
        if request.user.is_superadmin():
            return Order.objects.all()
        return Order.objects.filter(client=request.user)

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.client = request.user
        obj.save()

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Order, OrderAdmin)
