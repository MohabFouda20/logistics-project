from django.db import models

# Create your models here.
# Choices =[
#     ("wallet" , "wallet"),
#     ("cash" , "cash"),
#     ("bank transfer" , "bank transfer"),
# ]

class shipper(models.Model):
    shipper_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100 , null = False)
    phone = models.CharField(max_length=11 , null = False)
    email = models.EmailField(max_length=100 , null=True)
    pickup_address = models.CharField(max_length=200 , null = False)
    transfer_type = models.CharField(max_length=100 , null=True )
    product_type = models.CharField(max_length=100 , null=True)
    wallet_balance = models.FloatField(null=True)
    
