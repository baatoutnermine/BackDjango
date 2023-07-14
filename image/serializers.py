
from categorie.serializers import CategorySerializer
from image.models import Image
from djoser.serializers import UserSerializer
from rest_framework import serializers
class ImageSerializer(serializers.ModelSerializer):
    # user=UserSerializer(read_only=True)
 
    class Meta:
        model = Image
       
       
        exclude = ['image']