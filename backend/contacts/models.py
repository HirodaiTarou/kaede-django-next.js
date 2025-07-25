from django.db import models


class Contact(models.Model):
    """
    お問い合わせモデル
    database.mdの仕様に基づいて作成
    """

    id = models.AutoField(primary_key=True, verbose_name="コンタクトID")
    name = models.CharField(max_length=100, verbose_name="氏名")
    email = models.EmailField(verbose_name="メールアドレス")
    category = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="種類"
    )
    message = models.TextField(verbose_name="メッセージ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="問い合わせ時間")

    class Meta:
        db_table = "contacts"
        verbose_name = "お問い合わせ"
        verbose_name_plural = "お問い合わせ"

    def __str__(self):
        return f"{self.name} <{self.email}>"


# Create your models here.
