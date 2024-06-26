from rest_framework.response import Response
from rest_framework import generics,status
from .models import NoteModel
from .serializers import NoteSerializer
import math
from datetime import datetime

# implementing SQL methods too in Django

class Notes(generics.GenericAPIView):
    serializer_class = NoteSerializer
    queryset = NoteModel.objects.all()

    def get(self, request):
        notes = NoteModel.objects.all()
        serializer = self.serializer_class(notes, many=True)
        return Response({
            "notes":serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This creates and saves a new object based on the validated data
            # usually used in post method- to save the converted python data to json data into db 
            #and also used while updating the data like PUT method (POST and PUT uses save())
            return Response({"status":"success", "data":{"note":serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status":"fail", "messages":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


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
