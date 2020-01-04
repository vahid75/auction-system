from django.urls import path
from .views import bid_history,home,ItemDetails,ItemCreate,BidCreate

# app_name = 'core_app'


urlpatterns = [
    path('history/', bid_history,name = "history"),
    path('home/', home,name = "home"),
    path('details/<int:pk>/', ItemDetails.as_view(),name = "details"),
    path('bid/', BidCreate.as_view(),name = "item"),
    path('item/', ItemCreate.as_view(),name = "bid"),
    
]