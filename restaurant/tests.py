from django.test import TestCase

# Create your tests here.
class TestRestaurant(TestCase):

    def test_top_page(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_restaurant_top(self):
        res = self.client.get("/restaurant/")
        self.assertEqual(res.status_code, 200)