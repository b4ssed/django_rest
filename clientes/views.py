from django.shortcuts import render
from rest_framework import viewsets
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente

class ClientesViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer