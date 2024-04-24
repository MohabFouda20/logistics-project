from rest_framework import serializers
from .models import shipper

class shipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = shipper
        fields = '__all__'