from django.db import models


class Contact(models.Model):
    """
    お問い合わせモデル
    database.mdの仕様に基づいて作成
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    category = models.CharField(max_length=50, null=False, blank=True)
    message = models.TextField(max_length=2000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        db_table = "contacts"

    def __str__(self):
        return f"{self.name} <{self.email}>"
