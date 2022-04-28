from django.contrib import admin
from .models import Priceplan, Order


class PriceAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'plan_price')
    prepopulated_fields = {'slug': ('plan_name',)}


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20

# Register your models here.
admin.site.register(Priceplan, PriceAdmin ),
admin.site.register(Order)


