from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Review, ReviewLog


# Resource定義
class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review


class ReviewLogResource(resources.ModelResource):
    class Meta:
        model = ReviewLog


# Admin定義
@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    resource_class = ReviewResource


@admin.register(ReviewLog)
class ReviewLogAdmin(ImportExportModelAdmin):
    resource_class = ReviewLogResource
