from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User
from lectures.models import Lecture


class Review(models.Model):
    """
    レビュー
    """

    ATTENDANCE_CHOICES = [
        ("no", "no"),
        ("sometimes", "sometimes"),
        ("always", "always"),
    ]
    GRADE_CHOICES = [
        ("excellent", "excellent"),
        ("good", "good"),
        ("pass", "pass"),
        ("fail", "fail"),
        ("undecided", "undecided"),
    ]

    id = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name="reviews",
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews", null=False, blank=False
    )
    attendance_year = models.IntegerField(null=True, blank=True)
    attendance_confirm = models.CharField(
        max_length=20, choices=ATTENDANCE_CHOICES, null=False, blank=True
    )
    weekly_reports = models.BooleanField(null=True, blank=True)
    weekly_tests = models.BooleanField(null=True, blank=True)
    midterm_reports = models.BooleanField(null=True, blank=True)
    midterm_tests = models.BooleanField(null=True, blank=True)
    final_reports = models.BooleanField(null=True, blank=True)
    final_tests = models.BooleanField(null=True, blank=True)
    past_report_possession = models.BooleanField(null=True, blank=True)
    past_test_possession = models.BooleanField(null=True, blank=True)
    grades = models.CharField(
        max_length=20, choices=GRADE_CHOICES, null=False, blank=True
    )
    credit_level = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    interest_level = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    skill_level = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comments = models.TextField(max_length=1000, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        db_table = "reviews"

    def __str__(self):
        return f"{self.lecture.lecture_name} - {self.user.username}"


class ReviewLog(models.Model):
    """
    レビューログ（変更履歴）
    """

    ATTENDANCE_CHOICES = [
        ("no", "no"),
        ("sometimes", "sometimes"),
        ("always", "always"),
    ]
    GRADE_CHOICES = [
        ("excellent", "excellent"),
        ("good", "good"),
        ("pass", "pass"),
        ("fail", "fail"),
        ("undecided", "undecided"),
    ]

    id = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, null=False, blank=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    attendance_year = models.IntegerField(null=True, blank=True)
    attendance_confirm = models.CharField(
        max_length=20, choices=ATTENDANCE_CHOICES, null=False, blank=True
    )
    weekly_reports = models.BooleanField(null=True, blank=True)
    weekly_tests = models.BooleanField(null=True, blank=True)
    midterm_reports = models.BooleanField(null=True, blank=True)
    midterm_tests = models.BooleanField(null=True, blank=True)
    final_reports = models.BooleanField(null=True, blank=True)
    final_tests = models.BooleanField(null=True, blank=True)
    past_report_possession = models.BooleanField(null=True, blank=True)
    past_test_possession = models.BooleanField(null=True, blank=True)
    grades = models.CharField(
        max_length=20, choices=GRADE_CHOICES, null=False, blank=True
    )
    credit_level = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    interest_level = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    skill_level = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comments = models.TextField(max_length=1000, null=False, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        db_table = "review_logs"

    def __str__(self):
        return f"{self.lecture.lecture_name} - " f"{self.user.username} - {self.status}"


# Create your models here.
