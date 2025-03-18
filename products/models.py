from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(max_length=200)
    category=models.CharField(max_length=10)
    sub_category=models.CharField(max_length=10)
    qty=models.IntegerField()
    seller = models.ForeignKey(User,on_delete=models.CASCADE,related_name='seller',null=True,default=None)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

@receiver(models.signals.pre_delete, sender=ProductImage)
def delete_image_file(sender, instance, **kwargs):
    # Delete the associated image file
    instance.image.delete(save=False)


class Seller_user(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    shop_or_company_name = models.CharField(max_length=50)
    GST_number = models.CharField( max_length=20)
    shop_address= models.CharField(max_length=100)