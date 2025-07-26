from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Contact


# Resource定義
class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact


# Admin定義
@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    resource_class = ContactResource
