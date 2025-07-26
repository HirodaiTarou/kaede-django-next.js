from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User, UserLog
from django import forms


# ...existing code...

class UserCreationForm(forms.ModelForm):
    """
    ユーザー作成フォーム
    """
    password1 = forms.CharField(label='パスワード', widget=forms.PasswordInput)
    password2 = forms.CharField(label='パスワード（確認）', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'university_name', 'category', 'faculty', 'department', 'admission_year')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("パスワードが一致しません")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    ユーザー更新フォーム
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'university_name', 'category', 'faculty', 'department', 'admission_year', 'is_active', 'is_staff')


class UserAdmin(BaseUserAdmin):
    """
    ユーザー管理画面
    """
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'university_name', 'faculty', 'department', 'is_active', 'is_staff', 'created_at')
    list_filter = ('is_staff', 'is_active', 'university_name', 'faculty', 'created_at')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('個人情報', {'fields': ('username',)}),
        ('大学情報', {'fields': ('university_name', 'category', 'faculty', 'department', 'admission_year')}),
        ('権限', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('重要な日付', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'university_name', 'category', 'faculty', 'department', 'admission_year', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'username', 'university_name', 'faculty', 'department')
    ordering = ('email',)
    filter_horizontal = ()
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(User, UserAdmin)
admin.site.register(UserLog)
