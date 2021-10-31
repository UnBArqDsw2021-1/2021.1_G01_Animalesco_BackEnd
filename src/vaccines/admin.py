from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from vaccines.models import Vaccine


@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "application_date",
        "next_application_date",
        "pet",
        "is_finished",
    )
    search_fields = ("name", "application_dose")

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related("pet")
        return queryset
