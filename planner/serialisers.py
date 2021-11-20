from .models import Recipes
from rest_framework import serializers

class Recipe_Serialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Recipes
        fields= ['name']