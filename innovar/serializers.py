from rest_framework import serializers
from .validators import is_valid_cpf, is_valid_age
from .models import UsuarioCustomizado, HorarioBloqueado, Procedimento, Pacote, ClienteProcedimento, ClientePacote, HorarioBloqueado

class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = '__all__'

    def validate_cpf(self, value):
        # Implemente a validação personalizada do CPF aqui
        if not is_valid_cpf(value):
            raise serializers.ValidationError("CPF inválido")
        return value

    def validate_data_nascimento(self, value):
        # Implemente a validação personalizada da data de nascimento aqui
        if not is_valid_age(value):
            raise serializers.ValidationError("Data de nascimento inválida")
        return value

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
