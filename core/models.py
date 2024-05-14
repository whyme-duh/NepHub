from django.db import models

class Category(models.Model):
    # this is a model for a category class. Such as medical, education, ISP, etc.
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank = True, null= True)
    icon = models.ImageField(upload_to='icon')

    def __str__(self):
        return self.category_name


class Link(models.Model):
    # this consists of a links and has a relationship with Category class
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name