from sre_parse import CATEGORIES
from django.shortcuts import render
from categorie.models import Categorie
from rest_framework.response import Response 
from .serializers import CategorySerializer
from rest_framework.decorators import api_view, permission_classes
from django.urls import path,include
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


from categorie.serializers import CategorySerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def categorieList(request):
    categorie = Categorie.objects.all()
    serializer =CategorySerializer(categorie, many=True)
    return Response(serializer.data) 

