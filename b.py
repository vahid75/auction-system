import os, django,datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auction.settings")
django.setup()
from core_app.models import Item , Bid
from django.contrib.auth.models import User
from django.utils import timezone


def main():
    now = timezone.now()
    active_items = Item.objects.filter(status = "ACT") 
    for item in active_items:
        print(item.title)
        item.expire_by_date()

    all_users = User.objects.all()
    for user in all_users:
        user_active_items = user.item_set.filter(status = "ACT").count()
        item_limit_num = 2
        remining_permited_items = item_limit_num - user_active_items

        pks = user.item_set.filter(status = "INA",expire_date__lt=now).order_by('creation_date').values('pk')[:remining_permited_items]
        converted_items = user.item_set.filter(pk__in=(pks)).update(status = "ACT")
        

        """ 
        the last two lines takes so efforts beacuse we can't do this such easy by this code:

           user.item_set.filter(status = "INA").order_by('creation_date')[:remining_permited_items].update(status = "ACT")

        the reason is in sql databases you can't update the object and limit the same time like so:
            UPDATE ... WHERE ... LIMIT 5
        solution in this link:https://stackoverflow.com/questions/4285420/django-cannot-update-a-query-once-a-slice-has-been-taken by Jonny Buchanan

        """


        



if __name__ == "__main__":
    main()