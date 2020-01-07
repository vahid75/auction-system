from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns   
from .views import itemlist,item_detail,bidlist,item_bids

app_name = 'api'

urlpatterns = [
    path('itemlist/',itemlist),
    path('item_detail/<int:pk>/',item_detail),
    path('bidlist/',bidlist),
    path('item_bids/<int:pk>/',item_bids),  
    # path('itemlist/',itemlist),

]

urlpatterns = format_suffix_patterns(urlpatterns)
