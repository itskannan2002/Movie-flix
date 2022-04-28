from django.urls import reverse
from django.db import models
from accounts.models import Account
from store.models import Product




# Create your models here.
class Priceplan(models.Model):
    plan_name                      = models.CharField(max_length= 50, unique= True)
    slug                           = models.SlugField(max_length= 200, unique= True)
    plan_price                     = models.IntegerField()
    # plan valid in months 
    plan_valid                     = models.IntegerField()
    resolution                     = models.CharField(max_length= 200, unique= True,  null=True)
    download                       = models.CharField(max_length= 200, unique= True  , null=True)
    add                            = models.CharField(max_length= 200 , unique= True , null=True)
    sports                         = models.CharField(max_length= 200, unique= True , null=True)
    sound                          = models.CharField(max_length= 200 , unique= True, null=True)
   
   
    def __str__(self):
        return self.plan_name     

    def get_url(self):
        return reverse('payment_detail', args=[self.slug])

class Order(models.Model):
    user        = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    first_name     = models.CharField(max_length=50)
    last_name      = models.CharField(max_length=50)
    email          = models.EmailField(max_length=50)
    credit_card    = models.CharField(max_length=16)
    expire_date    = models.CharField(max_length=50)
    cvv            = models.CharField(max_length=50)

    def __str__(self):
	    return self.first_name + ' ' + self.last_name 