from django.db import models

# Create your models here.

# Promotion - Product -> M2M relationships
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    dicount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    MEMEBERSHIP_BRONZE = 'B'
    MEMEBERSHIP_CHOICES = [
        (MEMEBERSHIP_BRONZE, 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_day = models.DateField(null=True)
    memebership = models.CharField(
        max_length=1, choices=MEMEBERSHIP_CHOICES, default=MEMEBERSHIP_BRONZE)
    

class Order(models.Model):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        ("C", "Completed"),
        ("F", "Failed"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    name = models.CharField(max_length=255)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()



class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)