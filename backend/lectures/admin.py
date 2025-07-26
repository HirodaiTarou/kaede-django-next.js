from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Lecture, LectureDetail, LectureDetailTime


# Resource定義
class LectureResource(resources.ModelResource):
    class Meta:
        model = Lecture


class LectureDetailResource(resources.ModelResource):
    class Meta:
        model = LectureDetail


class LectureDetailTimeResource(resources.ModelResource):
    class Meta:
        model = LectureDetailTime


# Admin定義
@admin.register(Lecture)
class LectureAdmin(ImportExportModelAdmin):
    resource_class = LectureResource


@admin.register(LectureDetail)
class LectureDetailAdmin(ImportExportModelAdmin):
    resource_class = LectureDetailResource


@admin.register(LectureDetailTime)
class LectureDetailTimeAdmin(ImportExportModelAdmin):
    resource_class = LectureDetailTimeResource
