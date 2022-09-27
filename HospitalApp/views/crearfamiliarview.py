from rest_framework import status, views
from rest_framework.response import Response
from HospitalApp.serializers.familiarserializer import FamiliarSerializer

class CrearFamiliarView(views.APIView):
    def post (self,request):
        serializer=FamiliarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)