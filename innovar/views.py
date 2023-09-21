from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .validators import is_valid_cpf, is_valid_age
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
            # Antes de salvar o usuário, você pode adicionar sua lógica de validação personalizada aqui

            # Verifique se o CPF é válido (você pode usar uma função personalizada para isso)
            cpf = serializer.validated_data.get('cpf')
            if not is_valid_cpf(cpf):
                return Response({'cpf': 'CPF inválido.'}, status=status.HTTP_400_BAD_REQUEST)

            # Verifique a idade com base na data de nascimento
            data_nascimento = serializer.validated_data.get('data_nascimento')
            if not is_valid_age(data_nascimento):
                return Response({'data_nascimento': 'Data de nascimento inválida.'}, status=status.HTTP_400_BAD_REQUEST)

            # Outras validações personalizadas podem ser adicionadas aqui

            # Após a validação personalizada, salve o usuário
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Função para validar o CPF (você pode usar uma biblioteca como "validate-docbr")
def is_valid_cpf(cpf):
    # Implemente a lógica para validar o CPF aqui
    # Retorna True se o CPF for válido, False caso contrário
    return True  # Substitua por sua própria lógica de validação de CPF

# Função para verificar a idade com base na data de nascimento
def is_valid_age(data_nascimento):
    # Implemente a lógica para verificar a idade aqui
    # Retorna True se a idade for válida, False caso contrário
    return True  # Substitua por sua própria lógica de validação de idade

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