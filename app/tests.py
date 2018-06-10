from django.test import TestCase, Client

from .models import Item


class ItemModelTests(TestCase):

    def test_str(self):
        """
        __str__はnameそのものを返す
        """
        item_name = "Catan"
        item = Item(name=item_name)
        self.assertIs(item.__str__(), item_name)


class IndexPageTests(TestCase):

    def test_get(self):
        client = Client()
        response = client.get('/app/')
        self.assertIs(response.status_code, 200)
