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

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=254, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)

    # 大学情報
    university_name = models.CharField(max_length=100, null=False, blank=True)
    category = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.CharField(max_length=100, null=False, blank=True)
    department = models.CharField(max_length=100, null=False, blank=True)
    admission_year = models.IntegerField(null=True, blank=True)

    # システム情報
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # タイムスタンプ
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # カスタムマネージャー
    objects = UserManager()

    # 認証設定
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class UserLog(models.Model):
    """
    ユーザーログ（操作履歴）
    """

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    university_name = models.CharField(max_length=100, null=False, blank=True)
    category = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.CharField(max_length=100, null=False, blank=True)
    department = models.CharField(max_length=100, null=False, blank=True)
    admission_year = models.IntegerField(null=True, blank=True)
    action = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        db_table = "user_logs"

    def __str__(self):
        return f"{self.username} - {self.action}"
