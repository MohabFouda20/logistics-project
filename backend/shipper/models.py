from django.db import models

# Create your models here.
# Choices =[
#     ("wallet" , "wallet"),
#     ("cash" , "cash"),
#     ("bank transfer" , "bank transfer"),
# # ]
class Wallet(models.Model):
    blance = models.FloatField(null=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    
class shipper(models.Model):
    shipper_id = models.AutoField(primary_key=True)
    wallet = models.OneToOneField(Wallet, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100 , null = False)
    phone = models.CharField(max_length=11 , null = False)
    email = models.EmailField(max_length=100 , null=True)
    pickup_address = models.CharField(max_length=200 , null = False)
    product_type = models.CharField(max_length=100 , null=True)
    
