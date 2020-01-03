from django.test import TestCase
from .models import Item,Bid
from .views import *
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.


class ItemTest(TestCase):  

    def test_home(self):
        """
        this method is for testing the home view . if it works it should return 200 status code
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)


    def test_details(self):
        """
        this method is for testing the detailview view . if it returns 200 status code it means that the goal method can show object details clearly.
        """
        test_user= User.objects.create(username = 'test_user',password = "mmn98765#",email = 't@yah.com')
        item = Item.objects.create(title = 'test_title',owner = test_user,original_price = 1000)
        
        response = self.client.get(reverse('details',kwargs={'pk':item.pk}))
        self.assertEqual(response.status_code,200)
        

    def test_history_items(self):
        username =  'test_user'
        password = 'mmn98765#'
        test_user= User.objects.create(username = username)
        #",email = 't@yah.com')
        test_user.set_password(password)
        test_user.save()
        item = Item.objects.create(title = 'test_title',owner = test_user,original_price = 1000)
        self.client.login(username= username,password= password)
        response = self.client.get(reverse('history'))
        self.assertQuerysetEqual(response.context['items'],['<Item: test_title>'])


class Bid_test(TestCase):
    def test_history_bids(self):
        """
        this method test the (Bid,Item) models and bid_history view functionality
        if the objects created and sits on the client side vision,it assert that this view works as expected.  
        """
        test_user1= User.objects.create(username = 'test_user1',password = "mmn98765#",email = 't@yah.com')
        username =  'test_user2'
        password = 'mmn98765#'        

        test_user2= User.objects.create(username =username,email = 't@yah.com')
        test_user2.set_password(password)
        test_user2.save()

        item = Item.objects.create(title = 'test_title',owner = test_user1,original_price = 1000)
        bid = Bid.objects.create(item = item,offer_person = test_user2,offer_price = 2000 )

        self.client.login(username = username,password = password)
        response = self.client.get(reverse('history'))

        self.assertQuerysetEqual(response.context['bids'],["<Bid: test_user2's_bid>"])

    


        




        
