from rest_framework import serializers
from .models import InvoiceListModel,Item

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=InvoiceListModel
        fields=['clientName','totalAmount']
        
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=['description','rate','quantity']
        