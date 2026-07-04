from django.db import models
from django.utils.text import slugify               #ye builtin function ha django ka slug bnanay k liy
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)             
    slug = models.SlugField(unique=True, blank=True)          #yaha id ki jagha hum slug mobile_name etc us ekr skty hain 
    description = models.TextField(blank=True, null=False)    #blank b save ho ga or full b 
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args,**kwargs):       #arg argument ha or kwarg keyword ha 
        self.slug = slugify(self.name)      #yaha name ko slugify k sath pass kr dia or us k bad save method ko call kr dia jo parent class ka ha
        super().save(*args,**kwargs)         #super yaha parent class ka method call kr rha ha jo save ka ha or us k sath hum ne args or kwargs pass kr dia

    def __str__(self):
        return self.name  

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  #related_name ka mtlb ha k hum category k sath product ko access kr skty hain or us k sath products ka name rakh dia ha
    name = models.CharField(max_length=100 , unique=True)
    slug = models.SlugField(unique=True , blank=True)
    description = models.TextField(blank=True, null=False)
    price = models.DecimalField(max_digits=10 , decimal_places=2)  #max_digits ka mtlb ha k total kitny digits ho skty hain or decimal_places ka mtlb ha k kitny decimal places ho skty hain
    stock = models.PositiveIntegerField(default=0)  #ye field serf positive integer ko accept krta ha
    image = models.ImageField(upload_to='products/')  #image field jo products k liy upload krne k liy use ho 
    available = models.BooleanField(default=True)  #ye field ye check krta ha k product available ha ya nah
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Cart(models.Model):        #yaha auth isliy use krhy hain q k cart ik user ka hota ha 
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cart")       #yaha only one user ka data ho ga ya show ho ga 
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) #yaha foreign key relationships k liy
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1) #yaha default is liy use kiya  q k -eve ni use ho ga or 1 to car ho ga hi sai
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Processing", "Processing"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order Item: {self.product.name} - Quantity: {self.quantity}"
