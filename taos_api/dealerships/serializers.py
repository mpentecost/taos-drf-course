from rest_framework import serializers

from .models import Dealership, Auto, Sale
from people.serializers import PersonSerializer

class DealershipReadSerializer(serializers.ModelSerializer):
    """A Read serializer for the Dealership table"""
    general_manager = PersonSerializer()
    sales_reps = PersonSerializer(many=True)
    class Meta:
        model = Dealership
        fields = [
            'id',
            'name',
            'max_fleet_count',
            'is_active',
            'general_manager',
            'sales_reps'
        ]
    
class DealershipWriteSerializer(serializers.ModelSerializer):
    """A Write serializer for the Dealership table"""
    class Meta:
        model = Dealership
        fields = [
            'id',
            'name',
            'max_fleet_count',
            'is_active',
            'general_manager',
            'sales_reps',
            'web_users',
            'web_admin',
        ]

class AutoWriteSerializer(serializers.ModelSerializer):
    """A Write serializer for the Auto table"""
    class Meta:
        model = Auto
        fields = ['auto_model', 'auto_class', 'num_doors', 'dealer']


class AutoReadSerializer(serializers.ModelSerializer):
    """A Read serializer for the Auto Table"""
    dealer = DealershipReadSerializer()
    class Meta:
        model = Auto
        fields = ['id', 'auto_model', 'auto_class', 'num_doors', 'dealer']
