from django.contrib import admin
from .models import Product, Web
from .models import ReviewRating




# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

class WebAdmin(admin.ModelAdmin):
    list_display = ('web_name', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('web_name',)}




    
admin.site.register(Product, ProductAdmin),
admin.site.register(Web, WebAdmin),
admin.site.register(ReviewRating),


