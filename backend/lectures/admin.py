from django.contrib import admin
from .models import Lecture, LectureDetail, LectureDetailTime, Label, LectureLabel

admin.site.register(Lecture)
admin.site.register(LectureDetail)
admin.site.register(LectureDetailTime)
admin.site.register(Label)
admin.site.register(LectureLabel)
