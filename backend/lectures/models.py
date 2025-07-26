
from django.db import models


class Lecture(models.Model):
    """
    講義基本情報
    """
    id = models.AutoField(primary_key=True)
    lecture_name = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "lectures"

    def __str__(self):
        return self.lecture_name


class LectureDetail(models.Model):
    """
    講義詳細情報
    """
    id = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name="details"
    )
    lecture_code = models.CharField(max_length=50)
    syllabus_url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    faculty = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "lecture_details"

    def __str__(self):
        return f"{self.lecture.lecture_name} - {self.lecture_code}"


class LectureDetailTime(models.Model):
    """
    講義時間割情報
    """
    id = models.AutoField(primary_key=True)
    lecture_detail = models.ForeignKey(
        LectureDetail, on_delete=models.CASCADE, related_name="times"
    )
    year = models.IntegerField()
    term = models.CharField(max_length=20)
    day_of_week = models.CharField(max_length=10)
    time_period = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "lecture_detail_times"

    def __str__(self):
        return f"{self.year} {self.term} {self.day_of_week} {self.time_period}"
