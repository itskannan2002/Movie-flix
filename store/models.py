from category.models import category
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg
 


from django.db import models

# Create your models here.
class Product(models.Model):

    #normal details 
    product_name              = models.CharField(max_length= 200, unique= True)
    slug                      = models.SlugField(max_length= 200, unique= True)
    description               = models.TextField(max_length= 500, blank= True)
    image                     = models.ImageField(upload_to = 'photos/products')
    stock                     = models.IntegerField()
    is_available              = models.BooleanField(default=True)
    category                  = models.ForeignKey(category, on_delete=models.CASCADE)
    created_date              = models.DateTimeField(auto_now_add= True)
    modified_date             = models.DateField(auto_now=True)
    movie_release_year        = models.CharField(max_length=200, null=True, blank=True)
    tmdb                      = models.CharField(max_length=200, null=True, blank=True)


    product_director1         = models.CharField(max_length=200, null=True, blank=True)
    product_director2         = models.CharField(max_length=200, null=True, blank=True)


    #writer
    product_writer1         = models.CharField(max_length=100, null=True, blank=True)
    product_writer2         = models.CharField(max_length=100, null=True, blank=True)


    #producer
    movie_producer1         = models.CharField(max_length=100, null=True, blank=True)
    movie_producer2        = models.CharField(max_length=100, null=True, blank=True)


        
    # cast 
    product_actor1            = models.CharField(max_length=100, null=True, blank=True)
    actor1_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)

    product_actor2            = models.CharField(max_length=100, null=True, blank=True)
    actor2_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)

    product_actor3            = models.CharField(max_length=100, null=True, blank=True)
    actor3_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)

    product_actor4            = models.CharField(max_length=100, null=True, blank=True)
    actor4_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)

    product_actor5            = models.CharField(max_length=100, null=True, blank=True)
    actor5_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)

    product_actor6            = models.CharField(max_length=100, null=True, blank=True)
    actor6_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)


    product_actor1_image      = models.ImageField(upload_to = 'photos/products/cast')
    product_actor2_image      = models.ImageField(upload_to = 'photos/products/cast')
    product_actor3_image      = models.ImageField(upload_to = 'photos/products/cast')
    product_actor4_image      = models.ImageField(upload_to = 'photos/products/cast')
    product_actor5_image      = models.ImageField(upload_to = 'photos/products/cast')
    product_actor6_image      = models.ImageField(upload_to = 'photos/products/cast')

    movie_release_date        = models.CharField(max_length=20, null=True, blank=True)
 
    movie_link                = models.URLField(max_length=5000)

    movie_download_link_720p        = models.URLField(max_length=5000)
    movie_download_link_1080p       = models.URLField(max_length=5000)



    awards1      = models.CharField(max_length=100, default= '',null=True, blank=True)
    awards2      = models.CharField(max_length=100, default= '',  null=True, blank=True)
    awards3      = models.CharField(max_length=100, default= '', null=True, blank=True)
    awards4      = models.CharField(max_length=100, default= '', null=True, blank=True)
    awards5      = models.CharField(max_length=100, default= '', null=True, blank=True)
    awards6      = models.CharField(max_length=100, default= '',null=True, blank=True)



    nominee_awards1      = models.CharField(max_length=100, null=True, blank=True)
    nominee_awards2      = models.CharField(max_length=100, null=True, blank=True)
    nominee_awards3      = models.CharField(max_length=100, null=True, blank=True)

    




    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    def averagereview(self):
        reviews = ReviewRating.objects.filter(product=self, status = True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])

        return avg



class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=2000, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject



class Web(models.Model):

    #normal details 
    web_name              = models.CharField(max_length= 200, unique= True)
    slug                      = models.SlugField(max_length= 200, unique= True)
    description               = models.TextField(max_length= 500, blank= True)
    image                     = models.ImageField(upload_to = 'photos/products')
    stock                     = models.IntegerField()
    is_available              = models.BooleanField(default=True)
    category                  = models.ForeignKey(category, on_delete=models.CASCADE)
    created_date              = models.DateTimeField(auto_now_add= True)
    modified_date             = models.DateField(auto_now=True)
    movie_release_year        = models.CharField(max_length=200, null=True, blank=True)
    tmdb                      = models.CharField(max_length=200, null=True, blank=True)


    web_director1         = models.CharField(max_length=200, null=True, blank=True)
    web_director2         = models.CharField(max_length=200, null=True, blank=True)


    #writer
    web_writer1         = models.CharField(max_length=100, null=True, blank=True)
    web_writer2         = models.CharField(max_length=100, null=True, blank=True)


    #producer
    web_producer1         = models.CharField(max_length=100, null=True, blank=True)
    web_producer2        = models.CharField(max_length=100, null=True, blank=True)


        
    # cast 
    web_actor1            = models.CharField(max_length=100, null=True, blank=True)
    actor1_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)

    web_actor2            = models.CharField(max_length=100, null=True, blank=True)
    actor2_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)

    web_actor3            = models.CharField(max_length=100, null=True, blank=True)
    actor3_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)

    web_actor4            = models.CharField(max_length=100, null=True, blank=True)
    actor4_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)

    web_actor5            = models.CharField(max_length=100, null=True, blank=True)
    actor5_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)

    web_actor6            = models.CharField(max_length=100, null=True, blank=True)
    actor6_name_in_movie      = models.CharField(max_length=100, null=True, blank=True)


    web_actor1_image      = models.ImageField(upload_to = 'photos/products/cast')
    web_actor2_image      = models.ImageField(upload_to = 'photos/products/cast')
    web_actor3_image      = models.ImageField(upload_to = 'photos/products/cast')
    web_actor4_image      = models.ImageField(upload_to = 'photos/products/cast')
    web_actor5_image      = models.ImageField(upload_to = 'photos/products/cast')
    web_actor6_image      = models.ImageField(upload_to = 'photos/products/cast')

    movie_release_date        = models.CharField(max_length=20, null=True, blank=True)
 
    movie_link                = models.URLField(max_length=5000)

    
#awards 
    awards1      = models.CharField(max_length=100, null=True, blank=True)
    awards2      = models.CharField(max_length=100, null=True, blank=True)
    awards3      = models.CharField(max_length=100, null=True, blank=True)
    awards4      = models.CharField(max_length=100, null=True, blank=True)
    awards5      = models.CharField(max_length=100, null=True, blank=True)
    awards6      = models.CharField(max_length=100, null=True, blank=True)



    nominee_awards1      = models.CharField(max_length=100, null=True, blank=True)
    nominee_awards2      = models.CharField(max_length=100, null=True, blank=True)
    nominee_awards3      = models.CharField(max_length=100, null=True, blank=True)
    



    
    def get_url(self):
        return reverse('web_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.web_name