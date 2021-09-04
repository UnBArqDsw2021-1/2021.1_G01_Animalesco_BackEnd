from django.contrib import admin
from animals.models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'birth_date',
        'weight_kg',
        'owner',
        'tricks',
    )
