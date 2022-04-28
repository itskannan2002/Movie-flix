
from audioop import reverse
from email.policy import default
from django.db import models
from django.urls import reverse

# Create your models here.
class category(models.Model):
    category_name                = models.CharField(max_length=50)
    slug                         = models.SlugField(max_length=50, unique=True)
    description                  = models.TextField(max_length=250, blank=True)
    cat_image                    = models.ImageField(upload_to='photos/categories', blank=True)
    total_movie                  = models.IntegerField(default = 100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('products_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name