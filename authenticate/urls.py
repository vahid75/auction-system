from django.urls import path,include
import django.contrib.auth.urls
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import *



app_name = "authenticate"

urlpatterns= [


    path('accounts/',include('django.contrib.auth.urls')), 
    # path('',authenticating,name = "auth"),
    path("register/",register,name="reg"),    
    path("logout/",logoutnlogin,name = "logout"),   
    
    
]



# path('logout/',
    #     auth_views.LogoutView.as_view(next_page = reverse_lazy('chat:home')),name = 'logout'),          
    # path("accounts/password_change",auth_views.PasswordChangeView.as_view(
    #     success_url=reverse_lazy("auth:password_change_done")
    # ),name="password_change"),  