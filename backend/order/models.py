from django.db import models
from customer.models import clientData
from shipper.models import shipper

# Create your models here.
class order(models.Model):
    client = models.ForeignKey(clientData, on_delete=models.CASCADE)
    shipper = models.ForeignKey(shipper, on_delete=models.CASCADE)
    content = models.CharField(max_length=200 , null = False)
    cod = models.FloatField(max_length= 5, null = False , default=0)
    condtion = models.BooleanField(choices=[(True, 'Delivered'), (False, 'Not Delivered')], default=False)
    
    