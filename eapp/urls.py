from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from.api_views import CategoryViewSets, ProductViewSets, CartViewSets, CartItemViewSets, WishlistViewSets, ReviewViewSets, OrderViewSets, OrderItemViewSets

router = DefaultRouter()
router.register(r'categories',CategoryViewSets)
router.register(r'products',ProductViewSets)
router.register(r'carts',CartViewSets)
router.register(r'cart-items',CartItemViewSets)
router.register(r'wishlists',WishlistViewSets)
router.register(r'reviews',ReviewViewSets)
router.register(r'orders',OrderViewSets)
router.register(r'order-items',OrderItemViewSets)

urlpatterns = [
    path('',views.home,name='home'),
    path('api/', include(router.urls)),
    # #catogeries
    # path("categories/",views.category_list,name="category-list"),     #function based view is used here  for all categories
    # path("categories/<int:pk>/",views.category_detail,name="category-detail"), 
    #     #yaha init means yaha pr integer b use ho ga for one category

    # #Products
    # path("products/", views.product_list,name="product_list"),
    # path("products/<int:pk>/",views.product_detail,name="product-detail"),

    # #Cart
    # path("carts/",views.cart_list,name="cart_list"),
    # path("carts/<int:pk>/",views.cart_detail,name="cart-detail"),

    # #CartItem
    # path("cart-items/",views.cart_item_list,name="cart_item_list"),
    # path("cart-items/<int:pk>/",views.cart_item_detail,name="cart_item-detail"),

    # #Wishlist
    # path("wishlists/",views.wishlist_list,name="wishlist_list"), 
    # path("wishlists/<int:pk>/",views.wishlist_detail,name="wishlist-detail"),

    # #Review
    # path("reviews/",views.review_list,name="review_list"),
    # path("reviews/<int:pk>/",views.review_detail,name="review-detail"),

    # #Order
    # path("orders/",views.order_list,name="order_list"),
    # path("orders/<int:pk>/",views.order_detail,name="order-detail"),

    # #OrderItem
    # path("order-items/",views.order_item_list,name="order_item_list"),
    # path("order-items/<int:pk>/",views.order_item_detail,name="order_item-detail"),
]