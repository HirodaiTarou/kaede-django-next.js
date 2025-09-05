from django.test import TestCase
from contacts.models import Contact


class ContactModelTestCase(TestCase):
    def test_contact_model(self):
        """Contactモデルのテスト"""
        contact = Contact.objects.create(
            name="テストユーザー",
            email="test@example.com",
            category="general",
            message="テストメッセージ"
        )

        self.assertEqual(contact.name, "テストユーザー")
        self.assertEqual(contact.email, "test@example.com")
        self.assertEqual(contact.category, "general")
        self.assertEqual(contact.message, "テストメッセージ")
        self.assertTrue(contact.created_at)
