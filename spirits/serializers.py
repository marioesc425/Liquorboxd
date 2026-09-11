from rest_framework import serializers
from .models import Spirit

class SpiritSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spirit
        fields = ['id', 'name', 'category', 'brand', 'abv', 'description']