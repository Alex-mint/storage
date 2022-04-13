from django.contrib import admin

from main.models import CartProduct, Cart, Customer, Order, Item

admin.site.register(Item)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
