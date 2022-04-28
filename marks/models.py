from django.db import models
from store.models import Product
from accounts.models import Account




# Create your models here.
class Mark(models.Model):
    mark_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.mark_id

class MarkItem(models.Model):
    user        = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    mark        = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True)
    quantity    = models.IntegerField()
    is_active   = models.BooleanField(default = True)



    def sub_total(self):
        return self.quantity
        
        
    def __unicode__(self):
        return self.product