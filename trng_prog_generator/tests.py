from django.test import TestCase
from django.urls import resolve
from .views import home_page

# Create your tests here.
class HomeTest(TestCase):
    def test_home_url(self):
        view=resolve('/home/')
        self.assertEquals(view.func, home_page)
