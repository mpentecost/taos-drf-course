from rest_framework import serializers

from .models import Dealership, Auto, Sale

from people.serializers import PersonSerializer

class DealershipSerializer(serializers.ModelSerializer):
    """A serializer for the Dealership table"""
    general_manager = PersonSerializer()
    sales_reps = PersonSerializer(many=True, read_only=True)
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

class AutoSerializer(serializers.ModelSerializer):
    """A serializer for the Auto table"""
    dealer = DealershipSerializer()
    class Meta:
        model = Auto
        fields = ['id','auto_model', 'auto_class', 'num_doors', 'dealer']
