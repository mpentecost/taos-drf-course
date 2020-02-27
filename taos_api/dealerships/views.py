from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from common.models import ReadWriteSerializerMixin
from .serializers import AutoReadSerializer, AutoWriteSerializer
from .models import Auto


class AutoViewSet(ReadWriteSerializerMixin, viewsets.ModelViewSet):
    """Endpoints for the Auto model"""

    queryset = Auto.objects.all()
    read_serializer_class = AutoReadSerializer
    write_serializer_class = AutoWriteSerializer

    @action(detail=True, methods=['get'])
    def auto_test(self, request, pk=None):
        """Return some static message"""
        data = {'message': 'the route is working'}
        return Response(data)
