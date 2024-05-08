from django.db import models
import uuid


# Create your models here.

class InvoiceListModel(models.Model):
    invoiceNo = models.CharField(max_length=36,primary_key=True, default=uuid.uuid4,editable=False)
    clientName = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    totalAmount = models.IntegerField()
    
    
    
class Item(models.Model):
    invoiceNo = models.ForeignKey(InvoiceListModel, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    rate = models.IntegerField()
    quantity = models.IntegerField()
    total = models.IntegerField()