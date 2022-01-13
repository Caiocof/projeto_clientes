from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from clientes.serializers import ClienteSerializer
from clientes.models import Cliente


class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cpf', 'nome']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
