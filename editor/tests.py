from django.test import TestCase
from django.urls import reverse
from .views import execute_code

class EditorTests(TestCase):

    def test_execute_code_view(self):
        response = self.client.post(reverse('execute_code'), {
            'code': 'print("Hello, World!")',
            'input': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, World!', response.content.decode())

    def test_invalid_code(self):
        response = self.client.post(reverse('execute_code'), {
            'code': 'print(Hello, World!)',  # Missing quotes
            'input': ''
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.content.decode())

    def test_code_with_input(self):
        response = self.client.post(reverse('execute_code'), {
            'code': 'name = input(); print("Hello, " + name)',
            'input': 'Alice'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, Alice', response.content.decode())