from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, Cart, CartItem, Wishlist, Review , Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, CartItemSerializer, WishlistSerializer, ReviewSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsAdminUser]
    #Socho tum Amazon ke owner ho.
    # Category:Electronics ,Clothing ,Shoes
    # Kya normal customer nayi category bana sakta hai?
    # # ❌ Nahi.
    # # Sirf Admin bana sakta hai.
    # is liy adminuser use kiya ha 

class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticated, IsAdminUser]

    # Search + Filter + Ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Search
    search_fields = [
        "name",
        "description",
        "category__name",
    ]

    # Filtering
    filterset_fields = {
        "category": ["exact"],
        "price": ["gte", "lte"],
        "stock": ["gte", "lte"],
        "available": ["exact"],
    }

    # Ordering
    ordering_fields = [
        "price",
        "stock",
        "created_at",
        "updated_at",
        "name",
    ]

    # Default Ordering
    ordering = ["-created_at"]

class CartViewSets(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

class CartItemViewSets(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    # lookup_field = 'slug
    permission_classes = [IsAuthenticated]
    #or yaha is authenticated is liy use kiya ha k ye fields user put krta ha etc.

class WishlistViewSets(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    # lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

class OrderItemViewSets(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    # lookup_field = 'slug'
    permission_classes = [IsAuthenticated]







    