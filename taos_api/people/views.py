from rest_framework import viewsets

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """A Person Viewset"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
