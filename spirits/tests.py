from django.test import TestCase
from django.contrib.auth.models import User
from .models import Spirit, Review

class SpiritModelTest(TestCase):
    def test_str_returns_name(self):
        spirit = Spirit.objects.create(
            name="Test Vodka",
            category="Vodka",
            brand="Test Brand",
            abv=40.0
        )
        self.assertEqual(str(spirit), "Test Vodka")

class ReviewModelTest(TestCase):
    def test_str_returns_expected_format(self):
        user = User.objects.create_user(username='testuser', password='testpass123')
        spirit = Spirit.objects.create(
            name="Test Rum",
            category="Rum",
            brand="Test Brand",
            abv=35.0
        )
        review = Review.objects.create(
            user=user,
            spirit=spirit,
            rating=4.5,
            date_tried="2026-01-01"
        )
        self.assertEqual(str(review), "Test Rum review by testuser")

class SpiritListViewTest(TestCase):
    def test_spirit_list_returns_200(self):
        response = self.client.get('/spirits/')
        self.assertEqual(response.status_code, 200)

    def test_search_filters_results(self):
        Spirit.objects.create(name="Whiskey One", category="Whiskey", brand="Brand", abv=40.0)
        Spirit.objects.create(name="Vodka One", category="Vodka", brand="Brand", abv=37.5)
        response = self.client.get('/spirits/', {'q': 'Whiskey'})
        self.assertContains(response, "Whiskey One")
        self.assertNotContains(response, "Vodka One")