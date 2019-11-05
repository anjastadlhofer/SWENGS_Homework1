from hw1.yamod.models import Country
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country 
        fields = ['name']
