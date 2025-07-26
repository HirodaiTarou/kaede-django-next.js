from django.db import models
from users.models import User
from lectures.models import Lecture


class Review(models.Model):
    """
    レビュー
    """

    id = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        related_name="reviews",
        default=1  # デフォルト値を設定
    )
    attendance_year = models.IntegerField(
        blank=True, null=True
    )
    attendance_confirm = models.CharField(
        max_length=50, blank=True, null=True
    )
    weekly_assignments = models.CharField(
        max_length=200, blank=True, null=True
    )
    midterm_assignments = models.CharField(
        max_length=200, blank=True, null=True
    )
    final_assignments = models.CharField(
        max_length=200, blank=True, null=True
    )
    past_exam_possession = models.CharField(
        max_length=100, blank=True, null=True
    )
    grades = models.CharField(max_length=50, blank=True, null=True)
    credit_level = models.IntegerField(blank=True, null=True)
    interest_level = models.IntegerField(blank=True, null=True)
    skill_level = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reviews"

    def __str__(self):
        return f"{self.lecture.lecture_name} - {self.user.username}"


class ReviewLog(models.Model):
    """
    レビューログ（変更履歴）
    """

    id = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=1
    )
    attendance_year = models.IntegerField(
        blank=True, null=True
    )
    attendance_confirm = models.CharField(
        max_length=50, blank=True, null=True
    )
    weekly_assignments = models.CharField(
        max_length=200, blank=True, null=True
    )
    midterm_assignments = models.CharField(
        max_length=200, blank=True, null=True
    )
    final_assignments = models.CharField(
        max_length=200, blank=True, null=True
    )
    past_exam_possession = models.CharField(
        max_length=100, blank=True, null=True
    )
    grades = models.CharField(max_length=50, blank=True, null=True)
    credit_level = models.IntegerField(blank=True, null=True)
    interest_level = models.IntegerField(blank=True, null=True)
    skill_level = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "review_logs"

    def __str__(self):
        return (
            f"{self.lecture.lecture_name} - "
            f"{self.user.username} - {self.status}"
        )


# Create your models here.
