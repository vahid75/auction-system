from django.shortcuts import render
from .models import *
from django.views.generic import DetailView,CreateView
from django.urls import reverse_lazy

# Create your views here.

def bid_history(request):
    user = request.user
    bids = user.bid_set.all()    
    items = Item.objects.filter(owner = user)
    if items:
        for item in items:
            owner = item.owner
            original_price = item.original_price
            offers = item.bid_set.all()  
            total_bids =item.bid_set.all().count()
    else:
        owner = None
        original_price = None
        offers = None
        total_bids = None
        

    
    context = {
        'user':user,
        'bids':bids,
        'items':items,
        'owner':owner,
        'original_price':original_price,
        'offers':offers,
        'total_bids':total_bids,
        
    }

    return render(request,'core_app/bid_panel.html',context)



def home(request):
    # user = request.user
    items = Item.objects.all()
    context ={
        'items':items
    }
    return render(request,'core_app/home.html',context)


class ItemDetails(DetailView):
    model = Item
    template_name = 'core_app/itemdetail.html'
    context_object_name = 'item'



#Views for create Item and Bid objects
from django.contrib.auth.mixins import LoginRequiredMixin
class ItemCreate(LoginRequiredMixin,CreateView):
    template_name = 'core_app/item_create.html'
    model = Item
    fields = ['title', 'description', 'original_price']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BidCreate(LoginRequiredMixin,CreateView):
    template_name = 'core_app/bid_create.html'
    model = Bid
    fields = ['item', 'offer_price']
    success_url = reverse_lazy('history')
    
    def form_valid(self, form):
        form.instance.offer_person = self.request.user
        return super().form_valid(form)