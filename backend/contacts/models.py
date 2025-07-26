from django.db import models


class Contact(models.Model):
    """
    お問い合わせモデル
    database.mdの仕様に基づいて作成
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(
        max_length=50, blank=True, null=True
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact"

    def __str__(self):
        return f"{self.name} <{self.email}>"
