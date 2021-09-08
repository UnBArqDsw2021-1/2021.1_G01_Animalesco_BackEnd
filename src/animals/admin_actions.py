

def mark_as_proven_veracity(modeladmin, request, queryset):
    queryset.update(proven_veracity=True)