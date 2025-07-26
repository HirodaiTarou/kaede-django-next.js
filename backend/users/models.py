from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """
    カスタムユーザーマネージャー
    """

    def create_user(self, email, username, password=None, **extra_fields):
        """
        一般ユーザーを作成
        """
        if not email:
            raise ValueError('メールアドレスは必須です')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        スーパーユーザーを作成
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('スーパーユーザーはis_staff=Trueである必要があります')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('スーパーユーザーはis_superuser=Trueである必要があります')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    ユーザーモデル
    database.mdの仕様に基づいて作成
    """

    # 基本情報
    id = models.AutoField(primary_key=True, verbose_name='ID（主キー）')
    username = models.CharField(max_length=150, verbose_name='ユーザー名')
    email = models.EmailField(unique=True, verbose_name='メールアドレス')
    password = models.CharField(max_length=128, verbose_name='パスワード')

    # 大学情報
    university_name = models.CharField(max_length=100, verbose_name='大学名')
    category = models.CharField(max_length=50, verbose_name='所属')
    faculty = models.CharField(max_length=100, verbose_name='学部')
    department = models.CharField(max_length=100, verbose_name='学科')
    admission_year = models.IntegerField(verbose_name='入学年度')

    # システム情報
    is_active = models.BooleanField(default=True, verbose_name='アクティブ')
    is_staff = models.BooleanField(default=False, verbose_name='スタッフ')

    # タイムスタンプ
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成時間')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新時間')

    # カスタムマネージャー
    objects = UserManager()

    # 認証設定
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'

    def __str__(self):
        return self.username
