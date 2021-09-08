from django.contrib import admin

from animals.models import Specie
from animals.admin_actions import mark_as_proven_veracity


@admin.register(Specie)
class SpecieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'proven_veracity')
    search_fields = ('name',)
    list_filter = ('name', 'proven_veracity')

    actions = [
        mark_as_proven_veracity,
    ]
