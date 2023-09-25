from rest_framework import serializers
from .models import UsuarioCustomizado, HorarioBloqueado, Procedimento, Pacote, ClienteProcedimento, ClientePacote, HorarioBloqueado

class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class HorarioBloqueadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioBloqueado
        fields = '__all__'

class ProcedimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimento
        fields = '__all__'

class PacoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacote
        fields = '__all__'

class ClienteProcedimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteProcedimento
        fields = '__all__'

class ClientePacoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientePacote
        fields = '__all__'

class HorarioBloqueadoClientePacoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioBloqueado
        fields = '__all__'
        depth = 1

class UserAuthenticationSerializer(serializers.Serializer):
    cpf = serializers.CharField(max_length=14)
    password = serializers.CharField(write_only=True)

