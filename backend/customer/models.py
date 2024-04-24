from django.db import models
from shipper.models import shipper

# Create your models here.

    
    
class clientData(models.Model):
    egypt_governorates = [
    ("Cairo", "Cairo"),
    ("Alexandria", "Alexandria"),
    ("Giza", "Giza"),
    ("Sharqia", "Sharqia"),
    ("Qalyubia", "Qalyubia"),
    ("Ismailia", "Ismailia"),
    ("Suez", "Suez"),
    ("Dakahlia", "Dakahlia"),
    ("Beheira", "Beheira"),
    ("Aswan", "Aswan"),
    ("Asyut", "Asyut"),
    ("Beni Suef", "Beni Suef"),
    ("Faiyum", "Faiyum"),
    ("Gharbia", "Gharbia"),
    ("Luxor", "Luxor"),
    ("Matrouh", "Matrouh"),
    ("Minya", "Minya"),
    ("Monufia", "Monufia"),
    ("New Valley", "New Valley"),
    ("North Sinai", "North Sinai"),
    ("Port Said", "Port Said"),
    ("Qena", "Qena"),
    ("Red Sea", "Red Sea"),
    ("Sohag", "Sohag"),
    ("South Sinai", "South Sinai"),
    ("Kafr El Sheikh", "Kafr El Sheikh"),
    ("Damietta", "Damietta")
    ]
    
    shipper_id = models.ForeignKey(shipper, on_delete=models.CASCADE)
    name = models.CharField(max_length=100 , null = False)
    phone = models.CharField(max_length=11 , null = False)
    apartment = models.CharField(max_length=20 , null= True , blank= True)
    building_number = models.IntegerField(null  = True , blank= True)
    streetName = models.CharField(max_length=100 , null= True , blank= True)
    city = models.CharField(max_length=100 , null= True , blank= True)
    government =models.CharField(max_length=100 , null=False , choices=egypt_governorates)
    
    