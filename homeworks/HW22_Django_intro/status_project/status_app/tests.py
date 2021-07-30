from django.test import TestCase


# Create your tests here.
class TestStatusView(TestCase):
    def test_status_view(self):
        response = self.client.get(
            path=reversed('status')
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), 'Super good!')
