#from django.shortcuts import render

# Create your views here.

# modulos de DRF
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from petclub.models import Pet
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)



class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio

    def path(self, reuest):
        return Response(data="Hello gente estoy en patch", status=200)

    def delete(self, reuest):
        return Response(data="Hello gente estoy en delete", status=200)

    def post(self, reuest):
        return Response(data="Hello gente estoy en post", status=200)

class PetListAPIView(ListAPIView):

    def get(self, request):

        #return Response(data=pets, status =200)
        return Response(data="estas son las mascotas", status=200)

class PetAPIView(RetrieveAPIView):

    def get(self,request):
        return Response(data="Hello gente estoy en post", status=200)
