from django.db import models


class Lecture(models.Model):
    """
    講義基本情報
    """
    id = models.AutoField(primary_key=True)
    lecture_name = models.CharField(max_length=100, null=False, blank=False)
    teacher_name = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)

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
        Lecture,
        on_delete=models.CASCADE,
        related_name="details",
        null=False,
        blank=False,
    )
    lecture_code = models.CharField(max_length=20, null=False, blank=False)
    syllabus_url = models.URLField(max_length=200, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    grade = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)

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
        LectureDetail,
        on_delete=models.CASCADE,
        related_name="times",
        null=False,
        blank=False,
    )
    year = models.IntegerField(null=False, blank=False)
    term = models.CharField(max_length=20, null=False, blank=False)
    day_of_week = models.CharField(max_length=20, null=False, blank=False)
    time_period = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        db_table = "lecture_detail_times"

    def __str__(self):
        return f"{self.year} {self.term} {self.day_of_week} {self.time_period}"
