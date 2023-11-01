from ..models import  HorarioBloqueado
from rest_framework.serializers import ModelSerializer

class HorarioBloqueadoSerializer(ModelSerializer):
    class Meta:
        model = HorarioBloqueado
        fields = '__all__'