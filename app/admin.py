from django.contrib import admin

# Register your models here.
from .models import (
    Customer,
    Product,
    Order,
    Cart
)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','state','zipcode']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','desc','brand','category','image']

@admin.register(Cart)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','order_date','status']
