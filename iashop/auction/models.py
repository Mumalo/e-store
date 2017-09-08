from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .choices import ITEM_CONDITION_CHOICES, ITEM_STATUS_CHOICES, USER_GENDER_CHOICES
import arrow
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from base.models import BaseModel
from django.conf import settings
from django.db.models import Count
from smart_selects.db_fields import ChainedForeignKey



#
# class SystemUser(User):
#     phone = models.CharField(max_length=25)
#     institution = models.ForeignKey(Institution,
#                                     on_delete=models.CASCADE)
#     gender = models.CharField(choices=USER_GENDER_CHOICES, max_length=10)


# This is a multi-table imheritance since the parent class must also exist alone and in relation whith other classes

# class Buyer(SystemUser):
#     pass
#
# class Seller(SystemUser):
#     pass



# System users shall be able to place free adds on the site

class Category(BaseModel):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250, null=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d',blank=True, null=True)

    # return all subcategories under this category
    def custom_queryset(self):
        return self.subcategory.all()

    def __str__(self):
        return self.name

class SubCategory(BaseModel):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,related_name='subcat')

    def __str__(self):
        return self.name



# class Item(BaseModel):
#     name = models.CharField(max_length=250)
#     category = models.ForeignKey(Category,
#                                  on_delete=models.CASCADE)
#     description = models.TextField()
#
#     condition = models.CharField(max_length=10, choices=ITEM_CONDITION_CHOICES)
#     status = models.BooleanField(default=True)
#




class AuctionEvent(BaseModel):
    item = models.CharField(max_length=125, blank=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=True, related_name='cat_products')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True, related_name='sub_products')
    # sub_category = ChainedForeignKey(
    #     SubCategory,
    #     chained_field='category',
    #     chained_model_field='category',
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True,
    # )
    target_price = models.DecimalField(max_digits=8, decimal_places=2)
    start_price = models.DecimalField(max_digits=8, decimal_places=2)
    current_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    time = models.DateTimeField(default=timezone.now)
    available = models.BooleanField(default=True)
    description = models.TextField(max_length=250, null=True, blank=True)


    class Meta:
        ordering = ('-time',)

    def clean(self):
        auction_start_time = arrow.get(self.start_time)
        auction_end_time = arrow.get(self.end_time)
        auction_start_price = self.start_price

        if auction_start_time < arrow.utcnow() or auction_end_time < arrow.utcnow():
            raise ValidationError('Auction cannot be created in the past')
        if auction_end_time < auction_start_time:
            raise ValidationError('End time cannot be less than start time')
        if auction_start_time > auction_end_time:
            raise ValidationError('Start time cannot be greater than end time')

    def has_started(self):
        return self.start_time >= arrow.utcnow()



    def has_ended(self):
        current_time = arrow.utcnow()
        return  current_time > self.end_time

    def is_running(self):
        return self.has_started() and not self.has_ended()

    def time_left(self):
        if self.is_running():
            diff = self.end_time - arrow.utcnow()
            return diff.day
        else:
            return 'ended'


    def get_current_price(self):
        bids = Bid.objects.filter(event=self).order_by('-amount')
        count = bids.count()

        if count:
            current_price =  bids[0].amount
            return bids[0].amount
        else:
            return self.start_price

    def total_bids(self):
        return Bid.objects.filter(event=self).count()

    def winner(self):
        bids = Bid.objects.filter(event=self)
        count = bids.count()

        if self.has_ended():
            if count == 0:
                return "No one placed a bid on this item"
            elif count == 1:
                return bids[0].bidder
            else:
                return bids.order_by('-amount')[0].bidder
        else:
            return "No Winner yet"


    def __str__(self):
        return self.item











class Bid(BaseModel):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    bidder = models.ForeignKey(User,
                                on_delete=models.CASCADE, null=True, related_name='bidder')
    event = models.ForeignKey(AuctionEvent,
                              on_delete=models.CASCADE, null=True, related_name='bids')
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ('-created_at',)



     # Takes an argument and returns the current bid object
    # The current bid must be higher than the highest bid so far




class Advert(BaseModel):
    title = models.CharField(max_length=250, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='users/advert')
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='advert')
    available = models.BooleanField(default=False)


    class Meta:
        ordering = ('-last_created', )

    def __str__(self):
        return self.title

class BudgetPlan(Advert):
    pass










class Ratings(models.Model):
    time_frame = models.CharField(max_length=125, null=True)


