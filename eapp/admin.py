from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Wishlist, Review, Order, OrderItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(Review)
# ❌ admin.site.register(Order)  → yeh hata do

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)  # ✅ sirf yeh rakho

