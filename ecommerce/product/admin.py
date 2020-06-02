from django.contrib import admin
from .models import products, Catagory
# Register your models here.


class product_admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'catagory']
    search_field = ['name', 'catagory']
    list_filter = ('catagory',)


# admin.site.register(product_admin)
admin.site.register(products, product_admin)
admin.site.register(Catagory)
