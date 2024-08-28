from django.db import models
from django.contrib.auth.models import User
from cetagory_app.models import Cetagory
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='uploads/',null=True,blank = True)
    cetagory = models.ForeignKey(Cetagory,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class borrow_book(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_boroow')
    buy_book = models.ForeignKey(Book,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return self.buy_book.title
    
class comment(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    rat = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    Rating = models.CharField(max_length=40, choices=rat,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comments by{self.name}'