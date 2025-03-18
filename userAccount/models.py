from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='customer')
    address = models.CharField(max_length=80,blank=True)
    city = models.CharField(max_length=20, default="your city")
    state = models.CharField(max_length=20,default="your state")
    mobile = models.CharField(max_length=20,null=False,default="xxxxx-xxxxx")
    cart_items = models.ManyToManyField(Product, related_name='items',blank=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    qty = models.PositiveIntegerField()
    PAYMENT_CHOICES = [
        ('cash_on_delivery', 'Cash on Delivery'),
        ('debit_card', 'Debit Card'),
        ('credit_card', 'Credit Card'),
        ('upi','UPI')
    ]
    mode_of_payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    ORDER_CHOICES = [
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered','Delivered')
    ]
    order_status = models.CharField(max_length=20, choices=ORDER_CHOICES)