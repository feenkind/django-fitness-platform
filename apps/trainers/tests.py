from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
from apps.trainers.models import Trainer, Location


def create_trainer(username, visible=False):
    trainer_user = User.objects.create_user(
        username=username, password='12345'
    )
    return Trainer.objects.create(
        user=trainer_user,
        sport=Trainer.Sports.YOGA,
        motto='Test',
        about='Test',
        visible=visible,
    )


class TrainerListTestCase(TestCase):
    def test_empty_list(self):
        response = self.client.get(reverse('trainer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '0 results')
        self.assertQuerysetEqual(response.context['trainers'], [])
        self.assertQuerysetEqual(
            response.context['locations_by_trainerid'], []
        )

    def test_list_with_invisible_trainer(self):
        create_trainer('trainer_1')
        trainer_2 = create_trainer('trainer_2', True)

        response = self.client.get(reverse('trainer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1 result')
        self.assertQuerysetEqual(
            response.context['trainers'], [f'<Trainer: {trainer_2.__str__()}>']
        )
        self.assertQuerysetEqual(
            response.context['locations_by_trainerid'], []
        )

    def test_list_with_locations(self):
        trainer_1 = create_trainer('trainer_1', True)
        trainer_2 = create_trainer('trainer_2', True)

        location_1 = Location.objects.create(
            trainer=trainer_2,
            name='Test1',
            street='Street1',
            number='1',
            zipcode='12345',
            city='City1',
            country='Country1',
        )
        location_2 = Location.objects.create(
            trainer=trainer_2,
            name='Test2',
            street='Street2',
            number='2',
            zipcode='12345',
            city='City2',
            country='Country2',
        )

        response = self.client.get(reverse('trainer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '2 results')
        self.assertContains(response, 'Test1')
        self.assertContains(response, 'Test2')
        self.assertQuerysetEqual(
            response.context['trainers'],
            [
                f'<Trainer: {trainer_1.__str__()}>',
                f'<Trainer: {trainer_2.__str__()}>',
            ],
        )
        self.assertQuerysetEqual(
            response.context['locations_by_trainerid'],
            {
                str(trainer_2.id): [
                    f'<Location: {location_1.__str__()}>',
                    f'<Location: {location_2.__str__()}>',
                ]
            },
        )
