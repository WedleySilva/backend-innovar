from ..models import Pacote
from rest_framework.serializers import ModelSerializer

class PacoteSerializer(ModelSerializer):
    class Meta:
        model = Pacote
        fields = '__all__'