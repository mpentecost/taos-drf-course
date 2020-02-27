from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from common.models import ReadWriteSerializerMixin
from .serializers import AutoReadSerializer, AutoWriteSerializer
from .models import Auto


class AutoViewSet(ReadWriteSerializerMixin, viewsets.ModelViewSet):
    """Endpoints for the Auto model"""

    read_serializer_class = AutoReadSerializer
    write_serializer_class = AutoWriteSerializer

    def get_queryset(self):
        user = self.request.user
        prefetch_fields = ['dealer__sales_reps']
        select_related_fields = ['dealer__general_manager']

        queryset = (
            Auto.get_my_autos(user)
            .prefetch_related(*prefetch_fields)
            .select_related(*select_related_fields)
        )
        return queryset

    @action(detail=True, methods=['get'])
    def auto_test(self, request, pk=None):
        """Return some static message"""
        data = {'message': 'the route is working'}
        return Response(data)
