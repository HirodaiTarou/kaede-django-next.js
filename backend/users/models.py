from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from typing import Any


class UserManager(BaseUserManager):
    """
    ユーザーマネージャークラス。ユーザー作成・スーパーユーザー作成のロジックを定義。
    """

    def create_user(
        self, user_email: str, password: str | None = None, **extra_fields: Any
    ) -> 'User':
        """
        一般ユーザーを作成します。
        """
        if not user_email:
            raise ValueError('メールアドレスは必須です')
        user_email = self.normalize_email(user_email)
        user = self.model(user_email=user_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, user_email: str, password: str, **extra_fields: Any
    ) -> 'User':
        """
        スーパーユーザーを作成します。
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('スーパーユーザーはis_staff=Trueである必要があります')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('スーパーユーザーはis_superuser=Trueである必要があります')
        return self.create_user(user_email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    カスタムユーザーモデル。
    Laravelのシーダーファイルに基づいてフィールドを定義。
    """
    # 基本情報（Laravelシーダーに基づく）
    user_name: models.CharField = models.CharField(
        'ユーザー名',
        max_length=255,
        null=False,
        blank=False
    )
    user_email: models.EmailField = models.EmailField(
        'メールアドレス',
        unique=True,
        null=False,
        blank=False
    )
    
    # 大学・所属情報（Laravelシーダーに基づく）
    university_name: models.CharField = models.CharField(
        '大学名',
        max_length=255,
        null=False,
        blank=False
    )
    category: models.CharField = models.CharField(
        '所属',
        max_length=100,
        null=False,
        blank=False
    )
    faculty: models.CharField = models.CharField(
        '学部',
        max_length=100,
        null=False,
        blank=False
    )
    department: models.CharField = models.CharField(
        '学科',
        max_length=100,
        null=False,
        blank=False
    )
    admission_year: models.IntegerField = models.IntegerField(
        '入学年度',
        null=False,
        blank=False
    )
    
    # Django認証用フィールド
    is_active: models.BooleanField = models.BooleanField(
        'アカウント有効',
        default=True
    )
    is_staff: models.BooleanField = models.BooleanField(
        'スタッフ権限',
        default=False
    )
    
    # タイムスタンプ
    created_at: models.DateTimeField = models.DateTimeField(
        '作成時間',
        auto_now_add=True
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        '更新時間',
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS: list[str] = [
        'user_name',
        'university_name',
        'category',
        'faculty',
        'department',
        'admission_year'
    ]

    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'
        db_table = 'users'

    def __str__(self) -> str:
        return self.user_email

    def get_full_name(self) -> str:
        """ユーザーのフルネームを返す"""
        return self.user_name

    def get_short_name(self) -> str:
        """ユーザーの短縮名を返す"""
        return self.user_name
