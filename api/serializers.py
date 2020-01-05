from rest_framework import serializers
from core_app.models import Item,Bid

class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') 
    winner = serializers.ReadOnlyField() 
    class Meta:
        model = Item
        fields = ['owner','title' ,'description','original_price','winner']
        


class BidSerializer(serializers.ModelSerializer):    
    offer_person = serializers.ReadOnlyField(source='offer_person.username')
       
    class Meta:
        model = Bid
        fields = ['offer_person','item','offer_price' ]
        

