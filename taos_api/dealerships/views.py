from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import AutoSerializer
from .models import Auto


class AutoViewSet(viewsets.ModelViewSet):
    """Endpoints for the Auto model"""

    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

    @action(detail=True, methods=['get'])
    def auto_test(self, request, pk=None):
        """Return some static message"""
        data = {'message': 'the route is working'}
        return Response(data)
