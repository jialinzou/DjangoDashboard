from django.db import models

class UsersPerChannel(models.Model):
    date = models.DateField(primary_key=True)
    Other = models.IntegerField()
    Direct = models.IntegerField()
    Email = models.IntegerField()
    Organic_Search = models.IntegerField()
    Paid_Search = models.IntegerField()
    Referral = models.IntegerField()
    Social = models.IntegerField()
    
class TopPages(models.Model):
    Date = models.DateField()
    Title = models.CharField(max_length=200)
    Engaged_time = models.IntegerField()
    Unique_users = models.IntegerField()
    Path = models.CharField(max_length=200)
    class Meta:
        unique_together = ['Date', 'Title']

class Top4Posts(models.Model):
    rank = models.IntegerField(primary_key = True)
    pic = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    viral_unique = models.IntegerField()
    link = models.CharField(max_length=200)