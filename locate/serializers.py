'''
    File name: locate/serializers.py
    Author: Uday Singh
    Python Version: 2.7
'''

from rest_framework import serializers
from .models import locate

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = locate
        fields = '__all__'
        depth = 1