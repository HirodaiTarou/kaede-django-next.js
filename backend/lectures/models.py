
from django.db import models


class Lecture(models.Model):
    """
    講義基本情報
    """
    id = models.AutoField(primary_key=True, verbose_name="講義ID")
    lecture_name = models.CharField(max_length=200, verbose_name="授業名")
    teacher_name = models.CharField(max_length=100, verbose_name="主担当教員名")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新時間")

    class Meta:
        db_table = "lectures"
        verbose_name = "講義"
        verbose_name_plural = "講義"

    def __str__(self):
        return self.lecture_name


class LectureDetail(models.Model):
    """
    講義詳細情報
    """
    id = models.AutoField(primary_key=True, verbose_name="講義詳細ID")
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name="details", verbose_name="講義ID")
    lecture_code = models.CharField(max_length=50, verbose_name="講義コード")
    syllabus_url = models.URLField(blank=True, null=True, verbose_name="シラバスURL")
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name="開講場所")
    faculty = models.CharField(max_length=100, blank=True, null=True, verbose_name="開講部局")
    category = models.CharField(max_length=50, blank=True, null=True, verbose_name="科目区分")
    grade = models.CharField(max_length=20, blank=True, null=True, verbose_name="履修年次")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新時間")

    class Meta:
        db_table = "lecture_details"
        verbose_name = "講義詳細"
        verbose_name_plural = "講義詳細"

    def __str__(self):
        return f"{self.lecture.lecture_name} - {self.lecture_code}"


class LectureDetailTime(models.Model):
    """
    講義時間割情報
    """
    id = models.AutoField(primary_key=True, verbose_name="時間割ID")
    lecture_detail = models.ForeignKey(LectureDetail, on_delete=models.CASCADE, related_name="times", verbose_name="講義詳細ID")
    year = models.IntegerField(verbose_name="年度")
    term = models.CharField(max_length=20, verbose_name="ターム")
    day_of_week = models.CharField(max_length=10, verbose_name="曜日")
    time_period = models.CharField(max_length=20, verbose_name="時限")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新時間")

    class Meta:
        db_table = "lecture_detail_times"
        verbose_name = "講義時間割"
        verbose_name_plural = "講義時間割"

    def __str__(self):
        return f"{self.year} {self.term} {self.day_of_week} {self.time_period}"


class Label(models.Model):
    """
    ラベル
    """
    id = models.AutoField(primary_key=True, verbose_name="ラベルID")
    label_name = models.CharField(max_length=50, unique=True, verbose_name="ラベル名")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新時間")

    class Meta:
        db_table = "labels"
        verbose_name = "ラベル"
        verbose_name_plural = "ラベル"

    def __str__(self):
        return self.label_name


class LectureLabel(models.Model):
    """
    講義とラベルの多対多関連
    """
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, verbose_name="講義ID")
    label = models.ForeignKey(Label, on_delete=models.CASCADE, verbose_name="ラベルID")

    class Meta:
        db_table = "lecture_labels"
        verbose_name = "講義ラベル関連"
        verbose_name_plural = "講義ラベル関連"
        unique_together = ("lecture", "label")

    def __str__(self):
        return f"{self.lecture.lecture_name} <-> {self.label.label_name}"

# Create your models here.
