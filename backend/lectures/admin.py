from django.contrib import admin
from .models import Lecture, LectureDetail, LectureDetailTime

admin.site.register(Lecture)
admin.site.register(LectureDetail)
admin.site.register(LectureDetailTime)
