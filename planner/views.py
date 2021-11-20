from django.shortcuts import render
from .models import Recipes
from rest_framework import viewsets
from .serialisers import Recipe_Serialiser

# Create your views here.
class recipe_viewset(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = Recipe_Serialiser