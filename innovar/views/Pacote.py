from django.db.models.signals import post_save
from ..models import Pacote
from ..serializers import (
    PacoteSerializer,
)
from rest_framework.viewsets import ModelViewSet

class PacoteViewSet(ModelViewSet):
    queryset = Pacote.objects.all()
    serializer_class = PacoteSerializer
