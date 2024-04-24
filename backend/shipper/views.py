from django.shortcuts import render
from .models import shipper
from . serializers import shipperSerializer
from rest_framework import generics

# Create your views here.

class shipperList(generics.ListAPIView):
    queryset = shipper.objects.all()
    serializer_class = shipperSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
    
    
class shipperCreate(generics.CreateAPIView):
    queryset = shipper.objects.all()
    serializer_class = shipperSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class shipperDetail(generics.RetrieveAPIView):
    queryset = shipper.objects.all()
    serializer_class = shipperSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
class shipperUpdate(generics.UpdateAPIView):
    queryset = shipper.objects.all()
    serializer_class = shipperSerializer    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class shipperDelete(generics.DestroyAPIView):
    queryset = shipper.objects.all()
    serializer_class = shipperSerializer
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
