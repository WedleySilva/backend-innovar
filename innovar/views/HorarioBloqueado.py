from ..models import HorarioBloqueado
from ..serializers import (
    HorarioBloqueadoSerializer,
)
from rest_framework.viewsets import ModelViewSet

class HorarioBloqueadoViewSet(ModelViewSet):
    queryset = HorarioBloqueado.objects.all()
    serializer_class = HorarioBloqueadoSerializer
