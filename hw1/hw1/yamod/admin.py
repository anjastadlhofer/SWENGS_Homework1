from django.contrib import admin
from . import models
from hw1.yamod.models import Song, Country, Person

# Register your models here.

class SongAdmin(admin.ModelAdmin):
    pass
admin.site.register(Song, SongAdmin)

class CountryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Country, CountryAdmin)

class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, PersonAdmin)
