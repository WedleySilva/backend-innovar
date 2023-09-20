from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioCustomizadoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UsuarioCustomizado, Procedimento, Pacote, ClienteProcedimento, ClientePacote, HorarioBloqueado
from .serializers import (
    ProcedimentoSerializer,
    PacoteSerializer,
    ClienteProcedimentoSerializer,
    ClientePacoteSerializer,
    HorarioBloqueadoSerializer,
)

@api_view(['POST'])
@permission_classes([AllowAny])
def cadastrar_usuario(request):
    if request.method == 'POST':
        serializer = UsuarioCustomizadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

# Path: uploader/models.py  