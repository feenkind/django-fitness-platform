from django.test import TestCase
from django.urls import reverse
from apps.users.models import User


class UserSettingsTestCase(TestCase):
    def test_not_logged_in(self):
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please login')

    def test_logged_in(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your profile settings')