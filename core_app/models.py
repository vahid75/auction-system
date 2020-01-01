from django.db import models
from django.utils import timezone 
from django.conf import settings 
from django.contrib.auth.models import User
import datetime
from django.urls import reverse


# Create your models here.

class Item(models.Model):

    SOLD = "SLD"
    BOUGHT = "BOU"
    ACTIVE = "ACT"  
    INACTIVE = "INA"
    status_choices =[
        (SOLD,"sold"),
        (BOUGHT,"bought"),
        (ACTIVE,"active"),
        (INACTIVE,"inactive"),
        ]    
    delta = datetime.timedelta(days = 10) 
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255,null = True,blank = True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    creation_date = models.DateTimeField(default = timezone.now)
    expire_date = models.DateTimeField(null = True,blank = True)
    status = models.CharField(max_length = 3,choices = status_choices,default = ACTIVE) 
    duration = models.DurationField(null = True,blank = True,default = delta) 
    original_price = models.FloatField(null = True)  
    best_offer_price = models.FloatField(null = True,blank = True)
    winner =  models.CharField(max_length = 50,null = True,blank = True)


    def get_absolute_url(self):
        return reverse('details',args=[(self.pk)]) 


    def __str__(self):
        return self.title

    def expire_by_date(self):
        if self.expire_date ==None:
            if self.creation_date.day + self.duration.days <= timezone.now().day:
                print(self.title ,'is being sold')
                self.status = self.SOLD
                self.save()
        else:
            if self.expire_date.day <= timezone.now().day:
                print(self.title ,'is being sold')
                self.status = self.SOLD
                self.save() 
        


    def save(self,*args,**kwargs):
        # user = Person.objects.get(name = self.owner)             
        # if Item.objects.filter(status = self.ACTIVE).count() ==0:
        #    user.user_item_number = 0 
        #    user.save()  
        if self.owner.item_set.filter(status = self.ACTIVE).count() >= 2:
            self.status = self.INACTIVE        
        # user.user_item_number +=1
        # user.save() 
        # if self.best_offer_price == None:
        #     self.best_offer_price = self.original_price             
        super().save(*args,**kwargs)
        
    
            

# class Person(models.Model):
#     """this is a profile model for storing additioal data for our user such as [user_item_number] that indicate this user'item created to limiting him for creating additional items larger than 2.the implementation is set in Item model save method. """

#     user = models.OneToOneField(User,on_delete = models.CASCADE)
#     name = models.CharField(max_length = 255,null = True,blank = True)
#     user_item_number = models.IntegerField(default = 0) 


class Bid(models.Model):
    
    item = models.ForeignKey(Item,on_delete = models.CASCADE)
    offer_person = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    offer_price = models.FloatField(null = True) 


    # best_offer_price =  models.FloatField(null = True,blank=True) 
    def deactive(self):
        if Item.status == self.INACTIVE:
            self.item = None

    def __str__(self):
        return self.offer_person.username + "'s_bid"


    def save(self,*args,**kwargs):    
        if self.offer_price > self.item.best_offer_price:
            self.item.best_offer_price = self.offer_price            
            self.item.winner = self.offer_person.username 
            self.item.save()          

        else:
            raise IndexError('you should offer a price higher than the best price')      
        super().save(*args,**kwargs)
        



        
