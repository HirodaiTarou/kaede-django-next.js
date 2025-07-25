from django.db import models
from users.models import User
from lectures.models import Lecture


class Review(models.Model):
    """
    レビュー
    """

    id = models.AutoField(primary_key=True, verbose_name="ID（主キー）")
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name="reviews", verbose_name="講義ID"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="ユーザーID",
    )
    attendance_year = models.IntegerField(
        blank=True, null=True, verbose_name="受講年度"
    )
    attendance_confirm = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="出欠の有無"
    )
    weekly_assignments = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="毎回のレポート・テスト"
    )
    midterm_assignments = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="中間のレポート・テスト"
    )
    final_assignments = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="期末のレポート・テスト"
    )
    past_exam_possession = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="過去問の所持"
    )
    grades = models.CharField(max_length=50, blank=True, null=True, verbose_name="成績")
    credit_level = models.IntegerField(blank=True, null=True, verbose_name="単位取得")
    interest_level = models.IntegerField(blank=True, null=True, verbose_name="面白さ")
    skill_level = models.IntegerField(blank=True, null=True, verbose_name="スキル")
    comments = models.TextField(blank=True, null=True, verbose_name="コメント")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="投稿時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新時間")

    class Meta:
        db_table = "reviews"
        verbose_name = "レビュー"
        verbose_name_plural = "レビュー"

    def __str__(self):
        return f"{self.lecture.lecture_name} - {self.user.username}"


class ReviewLog(models.Model):
    """
    レビューログ（変更履歴）
    """

    id = models.AutoField(primary_key=True, verbose_name="ID（主キー）")
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, verbose_name="講義ID"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザーID")
    attendance_year = models.IntegerField(
        blank=True, null=True, verbose_name="受講年度"
    )
    attendance_confirm = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="出欠の有無"
    )
    weekly_assignments = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="毎回のレポート・テスト"
    )
    midterm_assignments = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="中間のレポート・テスト"
    )
    final_assignments = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="期末のレポート・テスト"
    )
    past_exam_possession = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="過去問の所持"
    )
    grades = models.CharField(max_length=50, blank=True, null=True, verbose_name="成績")
    credit_level = models.IntegerField(blank=True, null=True, verbose_name="単位取得")
    interest_level = models.IntegerField(blank=True, null=True, verbose_name="面白さ")
    skill_level = models.IntegerField(blank=True, null=True, verbose_name="スキル")
    comments = models.TextField(blank=True, null=True, verbose_name="コメント")
    status = models.CharField(max_length=50, blank=True, null=True, verbose_name="状況")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="投稿時間")

    class Meta:
        db_table = "review_logs"
        verbose_name = "レビューログ"
        verbose_name_plural = "レビューログ"

    def __str__(self):
        return f"{self.lecture.lecture_name} - {self.user.username} - {self.status}"


class Like(models.Model):
    """
    いいね
    """

    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, verbose_name="レビューID"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザーID")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="いいね時間")

    class Meta:
        db_table = "likes"
        verbose_name = "いいね"
        verbose_name_plural = "いいね"
        unique_together = ("review", "user")

    def __str__(self):
        return f"{self.review.id} - {self.user.username}"


class DeleteReviewRequest(models.Model):
    """
    レビュー削除リクエスト
    """

    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, verbose_name="レビューID"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザーID")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="報告時間")

    class Meta:
        db_table = "delete_review_requests"
        verbose_name = "レビュー削除リクエスト"
        verbose_name_plural = "レビュー削除リクエスト"
        unique_together = ("review", "user")

    def __str__(self):
        return f"{self.review.id} - {self.user.username}"


# Create your models here.
