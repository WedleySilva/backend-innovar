from ..models import Procedimento
from rest_framework.serializers import ModelSerializer

class ProcedimentoSerializer(ModelSerializer):
    class Meta:
        model = Procedimento
        fields = '__all__'