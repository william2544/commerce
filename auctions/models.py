from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name='creates',default='')
    name=models.CharField(max_length=200)
    image=models.URLField(default='')
    description=models.CharField(max_length=400)
    amount=models.OneToOneField('Bid',related_name='price',on_delete=models.CASCADE)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    status=models.BooleanField()
    watchlist=models.ManyToManyField(User,related_name='watchlists',null=True,blank=True)

    def __str__(self):
        return f"We sell {self.name} at a fear price of {self.amount}"

class Bid(models.Model):
    bid_amount=models.IntegerField()
    bid_time=models.DateTimeField(auto_now_add=True)
    bidder=models.ForeignKey(User,related_name='owner',on_delete=models.CASCADE)
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE,related_name='listingBid',default='',null=True,blank=True)
    

class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='authors',null=True,blank=True)
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE,related_name='listings',null=True,blank=True)
    message=models.CharField(max_length=300,null=True,blank=True)
    time=models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    type=models.CharField(max_length=200)

    def __str__(self):
        return self.type