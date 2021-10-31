# Register your models here.
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from baths.models import Bath


@admin.register(Bath)
class BathAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "bath_date",
        "next_bath_date",
        "location_bath",
    )
    search_fields = ("bath_date",)

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('pet')
        return queryset

    def get_pet_name(self, obj: Bath) -> str:
        return obj.pet.name
        
    get_pet_name.short_description = "Pet"
    get_pet_name.admin_order_field = "pet__name"