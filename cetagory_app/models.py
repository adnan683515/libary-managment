from django.db import models

# Create your models here.
class Cetagory(models.Model):
    cetagory_name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40,null=True,blank=True)
    
    def __str__(self):
        return self.cetagory_name
    