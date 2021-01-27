from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
from apps.trainers.models import Trainer


def create_trainer(visible=False):
    trainer_user = User.objects.create_user(
        username='trainer_user', password='12345'
    )
    return Trainer.objects.create(
        user=trainer_user,
        sport=Trainer.Sports.YOGA,
        motto='Test',
        about='Test',
        visible=visible,
    )


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


class UserFavoritesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )
        self.client.login(username='testuser', password='12345')

    def test_user_no_favorites(self):
        response = self.client.get(reverse('user_favorites'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'You don\'t have any favorite trainers yet.'
        )
        self.assertQuerysetEqual(response.context['favorites'], [])

    def test_user_has_favorites_visible(self):
        test_trainer = create_trainer(visible=True)
        test_trainer.set_flag(self.user)

        response = self.client.get(reverse('user_favorites'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Trainer picture')
        self.assertQuerysetEqual(
            response.context['favorites'], ['<Trainer: trainer_user>']
        )

    def test_user_has_favorites_invisible(self):
        test_trainer = create_trainer(visible=False)
        test_trainer.set_flag(self.user)

        response = self.client.get(reverse('user_favorites'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'You don\'t have any favorite trainers yet.'
        )
        self.assertQuerysetEqual(response.context['favorites'], [])
