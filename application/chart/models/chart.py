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
    
class Users_WH(models.Model):
    date = models.DateField(primary_key=True)
    Other = models.IntegerField()
    Direct = models.IntegerField()
    Email = models.IntegerField()
    Organic_Search = models.IntegerField()
    Paid_Search = models.IntegerField()
    Referral = models.IntegerField()
    Social = models.IntegerField()

class Users_MH(models.Model):
    date = models.DateField(primary_key=True)
    Other = models.IntegerField()
    Direct = models.IntegerField()
    Email = models.IntegerField()
    Organic_Search = models.IntegerField()
    Paid_Search = models.IntegerField()
    Referral = models.IntegerField()
    Social = models.IntegerField()
    
class Users_PVN(models.Model):
    date = models.DateField(primary_key=True)
    Other = models.IntegerField()
    Direct = models.IntegerField()
    Email = models.IntegerField()
    Organic_Search = models.IntegerField()
    Paid_Search = models.IntegerField()
    Referral = models.IntegerField()
    Social = models.IntegerField()
    
class Users_BI(models.Model):
    date = models.DateField(primary_key=True)
    Other = models.IntegerField()
    Direct = models.IntegerField()
    Email = models.IntegerField()
    Organic_Search = models.IntegerField()
    Paid_Search = models.IntegerField()
    Referral = models.IntegerField()
    Social = models.IntegerField()

class Users_ROL(models.Model):
    date = models.DateField(primary_key=True)
    Other = models.IntegerField()
    Direct = models.IntegerField()
    Email = models.IntegerField()
    Organic_Search = models.IntegerField()
    Paid_Search = models.IntegerField()
    Referral = models.IntegerField()
    Social = models.IntegerField()
    
class Users_RW(models.Model):
    date = models.DateField(primary_key=True)
    Other = models.IntegerField()
    Direct = models.IntegerField()
    Email = models.IntegerField()
    Organic_Search = models.IntegerField()
    Paid_Search = models.IntegerField()
    Referral = models.IntegerField()
    Social = models.IntegerField()

class Users_WE(models.Model):
    date = models.DateField(primary_key=True)
    Other = models.IntegerField()
    Direct = models.IntegerField()
    Email = models.IntegerField()
    Organic_Search = models.IntegerField()
    Paid_Search = models.IntegerField()
    Referral = models.IntegerField()
    Social = models.IntegerField()
    
#####################################
    
class TopPages(models.Model):
    Date = models.DateField()
    Title = models.CharField(max_length=200)
    Engaged_time = models.IntegerField()
    Unique_users = models.IntegerField()
    Path = models.CharField(max_length=200)
    class Meta:
        unique_together = ['Date', 'Title']

#####################################

class TopPosts_WH(models.Model):
    rank = models.IntegerField(primary_key = True)
    viral_unique = models.IntegerField()
    link = models.CharField(max_length=400)

class TopPosts_PVN(models.Model):
    rank = models.IntegerField(primary_key = True)
    viral_unique = models.IntegerField()
    link = models.CharField(max_length=400)

class TopPosts_RW(models.Model):
    rank = models.IntegerField(primary_key = True)
    viral_unique = models.IntegerField()
    link = models.CharField(max_length=400)

class TopPosts_BI(models.Model):
    rank = models.IntegerField(primary_key = True)
    viral_unique = models.IntegerField()
    link = models.CharField(max_length=400)

class TopPosts_ROL(models.Model):
    rank = models.IntegerField(primary_key = True)
    viral_unique = models.IntegerField()
    link = models.CharField(max_length=400)

class TopPosts_WE(models.Model):
    rank = models.IntegerField(primary_key = True)
    viral_unique = models.IntegerField()
    link = models.CharField(max_length=400)

class TopPosts_MH(models.Model):
    rank = models.IntegerField(primary_key = True)
    viral_unique = models.IntegerField()
    link = models.CharField(max_length=400)