from django.shortcuts import render
from .models import Userinfo 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import logout_then_login
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == "POST":
        userinfoo = Userinfo(request.POST)        
        if userinfoo.is_valid():            
            user = userinfoo.save(commit=False)            
            user.set_password(user.password)
            user.save() 
            # return HttpResponseRedirect(reverse("chat:auth"))
            return authenticating(request)
            # precissior 2:
                # from django.contrib.auth.models import User
                # username  =userinfoo.cleaned_data["username"]           
                # email = userinfoo.cleaned_data["email"]
                # password = userinfoo.cleaned_data["password"]
                # cleaned_user = User.objects.create_user(username,email,password)



    else:
        userinfoo = Userinfo()
    
    return render(request,"authenticate/register.html",{"userinfoo":userinfoo})


def authenticating(request):
    
    if request.method == "POST":        
        userinfoo = Userinfo(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        authed_user = authenticate(request , username = username , password = password)

        if authed_user is not None:
            login(request,authed_user)
            print("you are login as {}". format(username))            
            return HttpResponseRedirect(reverse("home"))

        # else:
        #     if User.objects.get(username = "{}".format(username)) is not None : 
        #         context = {
        #             "error":'password is incorrect',
        #             'userinfoo':userinfoo
        #         }
        #         userinfoo = Userinfo()
                

        #     else:
        #        userinfoo = Userinfo() 

        #     return render(request,"chat/login.html",context)
                 
        
        context = {
                    "userinfoo":userinfoo
                }
    else: 
        userinfoo = Userinfo()
        context = {
            "userinfoo":userinfoo,
            

        }
    
    return render(request,"authenticate/login.html",context)




def logoutnlogin(request):
    """
    Logout n login back
    """
    return logout_then_login(request,login_url = reverse('auth'))
