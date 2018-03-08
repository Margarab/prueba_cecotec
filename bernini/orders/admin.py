from django.contrib import admin
from .models import Order


class ProductInline(admin.TabularInline):
    model = Order.products.through

class MyAdminSite(admin.AdminSite):
    site_header = 'Zapatos Bernini'
    site_title = 'Orders'
    index_title = 'Manage orders'

def download_csv(modeladmin, request, queryset):
    for order in queryset:
        return order.get_csv()
download_csv.short_description = "Download order in CSV"

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'client',)
    exclude = ['client',]
    inlines = [
        ProductInline,
    ]
    actions = [download_csv]


    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.client = request.user
        obj.save()
        form.save_m2m()
        obj.send_email()

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Order, OrderAdmin)
