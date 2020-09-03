from django.contrib import admin
from shop.models import Product, Bill, BillItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(BillItem)
