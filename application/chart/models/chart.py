from django.db import models

class MonthView(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    desktop = models.IntegerField()
    mobile = models.IntegerField()
    total_2015 = models.IntegerField()
    total_2014 = models.IntegerField()
    
class MonthByMonth(models.Model):
    id = models.DateField(primary_key=True)
    actual = models.IntegerField()
    forest = models.IntegerField()
    
class Channel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    may_2015 = models.IntegerField()
    april_2015 = models.IntegerField()
    may_2014 = models.IntegerField()
    MoM = models.FloatField()
    YoY = models.FloatField()

class PageViewsPerHour(models.Model):
    id = models.DateTimeField(primary_key=True)
    page_views = models.IntegerField()
    
class VideoViews(models.Model):
    id = models.DateTimeField(primary_key=True)
    video_views = models.IntegerField()
    
class UsersPerChannelAndBrand(models.Model):
    date = models.DateField()
    Other = models.IntegerField()
    Direct = models.IntegerField()
    Email = models.IntegerField()
    Organic_Search = models.IntegerField()
    Paid_Search = models.IntegerField()
    Referral = models.IntegerField()
    Social = models.IntegerField()
    brand = models.IntegerField() # ga's view id
    class Meta:
        unique_together = ('date', 'brand')
    
class TopPages(models.Model):
    Date = models.DateField()
    Title = models.CharField(max_length=200)
    Engaged_time = models.IntegerField()
    Unique_users = models.IntegerField()
    Path = models.CharField(max_length=200)
    
    class Meta:
        unique_together = ('Date', 'Title')