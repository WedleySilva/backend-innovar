from rest_framework.decorators import api_view, permission_classes
from .serializers import UserAuthenticationSerializer
from rest_framework.views import APIView
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioCustomizadoSerializer
from rest_framework import viewsets
from .models import UsuarioCustomizado, Procedimento, Pacote, ClienteProcedimento, ClientePacote, HorarioBloqueado
from .serializers import (
    ProcedimentoSerializer,
    PacoteSerializer,
    ClienteProcedimentoSerializer,
    ClientePacoteSerializer,
    HorarioBloqueadoSerializer,
)

class UsuarioCustomizadoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioCustomizadoSerializer


class PacoteViewSet(viewsets.ModelViewSet):
    queryset = Pacote.objects.all()
    serializer_class = PacoteSerializer


class ProcedimentoViewSet(viewsets.ModelViewSet):
    queryset = Procedimento.objects.all()
    serializer_class = PacoteSerializer


class ClienteProcedimentoViewSet(viewsets.ModelViewSet):
    queryset = ClienteProcedimento.objects.all()
    serializer_class = ClienteProcedimentoSerializer


class ClientePacoteViewSet(viewsets.ModelViewSet):
    queryset = ClientePacote.objects.all()
    serializer_class = ClientePacoteSerializer


class HorarioBloqueadoViewSet(viewsets.ModelViewSet):
    queryset = HorarioBloqueado.objects.all()
    serializer_class = HorarioBloqueadoSerializer
