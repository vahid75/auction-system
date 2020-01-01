from django.urls import path
from .views import bid_history,home,ItemDetails


urlpatterns = [
    path('history/', bid_history,name = "history"),
    path('home/', home,name = "home"),
    path('details/<int:pk>/', ItemDetails.as_view(),name = "details"),
    
]