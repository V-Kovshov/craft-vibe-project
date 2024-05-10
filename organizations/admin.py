from django.contrib import admin

from organizations.models.organization import Organization


@admin.register(Organization)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner")
