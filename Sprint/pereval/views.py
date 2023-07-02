from rest_framework import viewsets

from .models import PerevalAdded
from .serializers import PerevalAddedSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer




