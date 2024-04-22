import pymongo.mongo_client
from rest_framework import generics,status
from rest_framework.response import Response
from .models import NoteModel
from .serializers import NoteSerializer
import math
from datetime import datetime
import pymongo     #for mongoDb



############################################################################################

#For MongoDb:


client = pymongo.MongoClient("mongodb+srv://lavanya4301:lavanya1034@Cluster0.workfq9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
dbname = client['notes']
collection = dbname['user_notes']


sample_notes={
    "title":"first",
    "description":"first trial"
}

collection.insert_one(sample_notes)

notes_got=collection.find({})

for note in notes_got:
    print(note["title"])
    
    
#############################################################################################

#code with api calls- when using mongo db , sql code is commented out which is below.
# and in proj- settings.py  the databse details for SQL is commented out.
#when using SQL do reverse. uncomment Settings.py database and eneable SQL data
# and comment this code and uncomment down code

#Mongo DB:


class NoteList(generics.GenericAPIView):
    serializer_class = NoteSerializer
    queryset = NoteModel.objects.all()

    def get(self, request):
        get_notes = collection.find({})
        
        for no in get_notes:
            print(no)
        return Response({
            "status":"success"
        })

    def post(self, request):
        collection.insert_one(request.data)
        return Response({"status":"success"},status=status.HTTP_400_BAD_REQUEST)


###################################################################################################


#using SQL db


# class NoteList(generics.GenericAPIView):
#     serializer_class = NoteSerializer
#     queryset = NoteModel.objects.all()

#     def get(self, request):
#         notes = NoteModel.objects.all()
#         serializer = self.serializer_class(notes, many=True)
#         return Response({
#             "notes":serializer.data
#         })

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()  # This creates and saves a new object based on the validated data
#             # usually used in post method- to save the converted python data to json data into db 
#             #and also used while updating the data like PUT method (POST and PUT uses save())
#             return Response({"status":"success", "data":{"note":serializer.data}}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"status":"fail", "messages":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(generics.GenericAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer

    def get_note(self, pk):
        try:
            return NoteModel.objects.get(pk=pk)
        except:
            return None
        
    def get(self, request, pk):
        note = self.get_note(pk=pk)
        if note==None:
            return Response({"status":"fail", f"message":"Note with ID: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(note)
        return Response({"status":"success", "data":{"note":serializer.data}})
    
    def patch(self, request, pk):
        note = self.get_note(pk)
        if note==None:
            return Response({"status":"fail", f"message":"Note with ID: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status":"success", "data":{"note":serializer.data}})
        return Response({"status":"fail", "message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        note = self.get_note(pk)
        if note==None:
            return Response({"status":"fail", f"message":"Note with ID: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        note.delete()
        return Response({"status":"deleted"},status=status.HTTP_204_NO_CONTENT)
