from hw1.yamod.models import Country, Song, Person
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country 
        fields = ['name']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song 
        fields = ['title', 'genre', 'release_date', 'country', 'singers']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person 
        fields = ['first_name', 'last_name', 'year_of_birth']
