from .models import Categorie
from rest_framework import serializers

# Rest of your code


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorie
        fields = '__all__' 
       

       