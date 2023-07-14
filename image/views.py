from django.shortcuts import render
from image.models import Image
from image.serializers import ImageSerializer
from rest_framework import generics
from rest_framework.response import Response  
from rest_framework.decorators import api_view, permission_classes , parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework import filters


# affichage des images 
@api_view(['GET'])
@permission_classes([IsAuthenticated])# il faut passer token dans le head
def imageList(request):
    annonce = Image.objects.all()
    serializer =ImageSerializer(annonce, many=True)
    return Response(serializer.data)



#ajout d'une image 
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # il faut passer token dans le head
@parser_classes([JSONParser])
def CreateImage(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user) 
        return Response(serializer.data)  
    return Response(serializer.errors)

#filtrage des images par categorie
@api_view(['GET'])
@permission_classes([AllowAny])
def find_image (request,pk):
    images = Image.objects.filter(categorie_id=pk)
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

#filtrage des images par tags
class tagsSearch(generics.ListAPIView):
    
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends =[ filters.SearchFilter]
    search_fields=['tags']