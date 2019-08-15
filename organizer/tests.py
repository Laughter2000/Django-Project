from django.test import TestCase

# Create your tests here.
from .views import StartupDetail
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.
class TemplateTest(TestCase):
	def test_home_page_returns_correct_html(self):
		request = HttpRequest() 
		response = StartupDetail(request)
		expected_html = render_to_string('startup_detail.html')  
		self.assertEqual(response.content.decode(), expected_html) 
