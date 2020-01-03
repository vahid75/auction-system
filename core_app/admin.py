from django.contrib import admin
from .models import Item,Bid
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# class PersonInline(admin.StackedInline):
#     model = Person
#     can_delete = False
#     verbose_name_plural = 'person'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (PersonInline,)


    
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(Item)
admin.site.register(Bid)
