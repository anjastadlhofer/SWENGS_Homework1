from django.contrib import admin
from . import models
from hw1.yamod.models import Song, Country, Person

# Register your models here.

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date',)
    list_filter = ('singers',)
    search_fields = ('title',)
    sortable_by = ['title']
admin.site.register(Song, SongAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Country, CountryAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'year_of_birth')
admin.site.register(Person, PersonAdmin)
