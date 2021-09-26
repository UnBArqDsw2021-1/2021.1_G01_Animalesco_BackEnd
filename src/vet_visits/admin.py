from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from vet_visits.models import VetVisit


# Register your models here.
@admin.register(VetVisit)
class MedicineAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "vet_clinic",
        "description",
        "visit_date",
        "next_visit_date",
        "pet",
    )
    search_fields = ("id", "vet_clinic", "visit_date", "pet")

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('pet')
        return queryset