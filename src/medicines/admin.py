# Register your models here.
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from medicines.models import Medicine


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "start_date",
        "finish_date",
        "aplication_time",
        "pet",
    )
    search_fields = ("name",)

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related("pet")
        return queryset

    def get_pet_name(self, obj: Medicine) -> str:
        return obj.pet.name

    get_pet_name.short_description = "Pet"
    get_pet_name.admin_order_field = "pet__name"
