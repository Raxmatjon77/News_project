from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_news_page_status_code(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code,200)