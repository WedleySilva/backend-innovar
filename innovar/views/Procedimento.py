from ..models import Procedimento
from ..serializers import (
    ProcedimentoSerializer,
)
from rest_framework.viewsets import ModelViewSet

class ProcedimentoViewSet(ModelViewSet):
    queryset = Procedimento.objects.all()
    serializer_class = ProcedimentoSerializer
