from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UsuarioCustomizado, Procedimento, Pacote, ClienteProcedimento, ClientePacote, HorarioBloqueado
from .serializers import (
    UsuarioCustomizadoSerializer,
    ProcedimentoSerializer,
    PacoteSerializer,
    ClienteProcedimentoSerializer,
    ClientePacoteSerializer,
    HorarioBloqueadoSerializer, 
)

class UsuarioCustomizadoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioCustomizadoSerializer
    # permission_classes = [IsAuthenticated]
class ProcedimentoViewSet(viewsets.ModelViewSet):
    queryset = Procedimento.objects.all()
    serializer_class = ProcedimentoSerializer
    # permission_classes = [IsAuthenticated]
class PacoteViewSet(viewsets.ModelViewSet):
    queryset = Pacote.objects.all()
    serializer_class = PacoteSerializer
    # permission_classes = [IsAuthenticated]
class ClienteProcedimentoViewSet(viewsets.ModelViewSet):
    queryset = ClienteProcedimento.objects.all()
    serializer_class = ClienteProcedimentoSerializer
    # permission_classes = [IsAuthenticated]
class ClientePacoteViewSet(viewsets.ModelViewSet):
    queryset = ClientePacote.objects.all()
    serializer_class = ClientePacoteSerializer
    # permission_classes = [IsAuthenticated]
class HorarioBloqueadoViewSet(viewsets.ModelViewSet):
    queryset = HorarioBloqueado.objects.all()
    serializer_class = HorarioBloqueadoSerializer
    # permission_classes = [IsAuthenticated]
 
