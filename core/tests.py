from django.test import TestCase
from . models import Link, Category
# Create your tests here.

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(category_name ="Medical Link", icon ="image.jpg" )
        Category.objects.create(category_name ="Education Link", icon ="image1.jpg" )


class LinkTestCase(TestCase):
    def setUp(self):
        Link.objects.create(category="Medical Link", name ="Bir Hospital", link = "www.youtube.com" )
        Link.objects.create(category="Education Link", name ="teaching education", link = "www.youtube.com" )