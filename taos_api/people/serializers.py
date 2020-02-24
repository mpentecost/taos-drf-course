from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    """A serialzer for the Person model"""
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'age']
