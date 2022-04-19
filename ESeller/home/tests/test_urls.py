import unittest
from django.urls import reverse, resolve
from home.views import *


class TestUrls(unittest.TestCase):

    def test_fruit_url_is_resolved(self):
        url = reverse('fish')
        self.assertEquals(resolve(url).func.view_class, fish)


if __name__ == "__main__":
    unittest.main()