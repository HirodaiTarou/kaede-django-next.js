# from django.test import TestCase
# from contacts.models import Contact


# class ContactModelTestCase(TestCase):
#     def test_contact_model(self):
#         response = self.client.post(
#             "api/v1/contacts/",
#             {
#                 "name": "テストユーザー",
#                 "email": "test@example.com",
#                 "category": "general",
#                 "message": "テストメッセージ"
#             }
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertTrue(Contact.objects.filter(email="test@example.com").exists())
