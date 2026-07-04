from rest_framework import serializers
from.models import Category, Product, Cart, CartItem, Wishlist, Review, Order, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True) #imp
    #Har Order ke saare OrderItems bhi saath bhejo.
       #many=true ka matlab hai ki ek Order me multiple OrderItems ho sakte hai.
#To read_only=True ki wajah se DRF items ko ignore karega. Agar tum POST ke through nested
#  objects create karna chahte ho,
#  to custom create() method likhna padta hai.
    class Meta:
        model = Order
        fields = '__all__'



#yaha model ko json me convert karne ke liye serializers ka use kiya hai.