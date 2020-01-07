from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer,BidSerializer
from core_app.models import Item,Bid
# Create your views here.

@api_view(['GET','POST'])
def itemlist(request,format=None):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items,many = True)                
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data = request.data)        
        if serializer.is_valid():
            serializer.save(owner = request.user)            
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE','GET','PUT'])
def item_detail(request,pk,format = None):
    try :
        item = Item.objects.get(pk = pk)
    except Item.DoesNotExist:
        return  Response(status = status.HTTP_404_NOT_FOUND)     

    if request.method == 'GET':        
        serializer = ItemSerializer(item)                
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(item,data = request.data)
        serializer.owner = request.user
        if serializer.is_valid():
            serializer.save(owner = request.user)            
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if request.user.id == item.owner.id:
            item.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def bidlist(request,format=None):
    """ 
    With this view you can see your bids and can create a new bid with post method.
    """    
    if request.method == 'GET':
        bids = Bid.objects.filter(offer_person = request.user)
        serializer = BidSerializer(bids,many = True)                
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BidSerializer(data = request.data)        
        if serializer.is_valid():
            serializer.save(offer_person = request.user)            
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def item_bids(request,pk,format=None):
    """
    if the person that request a GET method is not the item owner,only some litle detail of the item bids is shown to him such total bids for that item ,the item owner name ,winner of that bid and  best offer price. 
    """
    item = Item.objects.get(pk = pk)
    if item.owner == request.user:
        if request.method == 'GET':
            item_bids = item.bid_set.all()
            serializer = BidSerializer(item_bids,many = True)          
            return Response(serializer.data)

    else:
        if request.method == 'GET':
            item_bids = item.bid_set.count()
            content = {'total bids for this item': item_bids,'item title':item.title,
                        'bid winner':item.winner,'best offer price':item.best_offer_price}            
            return Response(content)

