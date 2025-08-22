# users/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


class JWTAuthenticationTestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpass123',
            'university_name': '東京大学',
            'category': '国立'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_login_success(self):
        """正常ログインテスト"""
        url = reverse('token_obtain_pair')
        data = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

        # トークンが文字列であることを確認
        self.assertIsInstance(response.data['access'], str)
        self.assertIsInstance(response.data['refresh'], str)

    def test_login_invalid_credentials(self):
        """無効な認証情報でのログインテスト"""
        url = reverse('token_obtain_pair')
        data = {
            'email': self.user_data['email'],
            'password': 'wrongpassword'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_refresh_success(self):
        """トークン更新成功テスト"""
        # まずログインしてrefreshトークンを取得
        login_url = reverse('token_obtain_pair')
        login_data = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }
        login_response = self.client.post(login_url, login_data, format='json')
        refresh_token = login_response.data['refresh']

        # トークン更新をテスト
        refresh_url = reverse('token_refresh')
        refresh_data = {'refresh': refresh_token}

        response = self.client.post(refresh_url, refresh_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_token_refresh_invalid_token(self):
        """無効なリフレッシュトークンテスト"""
        url = reverse('token_refresh')
        data = {'refresh': 'invalid_token'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserModelTestCase(TestCase):
    """Userモデルのテスト"""

    def test_create_user(self):
        """ユーザー作成テスト"""
        user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpass123',
            'university_name': '東京大学',
            'category': '国立'
        }

        user = User.objects.create_user(**user_data)

        self.assertEqual(user.email, user_data['email'])
        self.assertEqual(user.username, user_data['username'])
        self.assertEqual(user.university_name, user_data['university_name'])
        self.assertTrue(user.check_password(user_data['password']))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
