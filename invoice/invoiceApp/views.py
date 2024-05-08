from django.shortcuts import render

from .models import InvoiceListModel, Item
from .serializers import InvoiceSerializer, ItemSerializer
from rest_framework import generics, status
from rest_framework.response import Response
import pymongo
from datetime import datetime
from bson import ObjectId


# Create your views here.

# mongo db connection:

Client = pymongo.MongoClient(
    "mongodb+srv://lavanya4301:lavanya1034@cluster0.workfq9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
dbname = Client["invoices"]
collection = dbname["invoice_list"]


class SetInvoice(generics.GenericAPIView):
    def post(self, request):
        print(request.data)
        entry = InvoiceSerializer(data=request.data)
        if entry.is_valid():
            print(entry.validated_data)
            entry.validated_data['date'] = datetime.now()
            entry = collection.insert_one(entry.validated_data)
            return Response(
                {"status": "success"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response({"status":entry.errors},status=status.HTTP_400_BAD_REQUEST)
    
class GetInvoice(generics.GenericAPIView):
    #getting all documents from collection 
    def get(self,request):
        entries = collection.find({})
        print(entries)
        invoice_serialized = [InvoiceSerializer(inv).data for inv in entries]
        return Response({
            "status":"success",
            "data":{"notes":invoice_serialized}
        })  
        
        
        
    #option  to delete all documents from collection
    def delete(self,request):
        collection.delete_many({})
        return Response({"status":"success"})
    
class OneInvoice(generics.GenericAPIView):   
    
    def get_invoice(self,pk):
        inpData = ObjectId(pk)
        try:
            return collection.find_one({"_id":inpData})
        except:
            return None
           
    #getting single document based on condition 
    def get(self,request,pk):
        print(pk)
        inv = self.get_invoice(pk=pk)
        if inv is not None:
            inv['_id']= str(inv['_id'])
            invoice_serialized = InvoiceSerializer(data=inv)
            if invoice_serialized.is_valid():
                return Response({
                    "status":"success",
                    "data":{"notes":invoice_serialized.validated_data}
                    
                })
            return Response({
                "status":"fail"
            },status=status.HTTP_400_BAD_REQUEST)     
            

    
class InvoiceAddItem(generics.GenericAPIView):
    def get_inv(self,pk): #check whether that invoice id is present or`` not
        try:
            return collection.find_one({"_id":ObjectId(pk)})
        except:
            return None
    def post(self,request,pk):
        inv_match = self.get_inv(pk=pk)
        if inv_match is not None:  #if invoice is present
            item_data = request.data
            # item_data['_id'] = str(inv_match['_id'])
            print(item_data)
            collection.insert_one(item_data)
            return Response({"status":"success"},status=status.HTTP_200_OK)
           
            # serializer = ItemSerializer(data=item_data)
            # if serializer.is_valid():
            #     print(serializer.validated_data)
            #     collection.insert_one(serializer.validated_data)
            #     return Response({"status":"success","data":{"item":serializer.validated_data}},status=status.HTTP_200_OK)
            # else:
            #      return Response({"status":"fail","error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status":"fail"},status=status.HTTP_400_BAD_REQUEST)