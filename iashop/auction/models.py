from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .choices import ITEM_CONDITION_CHOICES, ITEM_STATUS_CHOICES, USER_GENDER_CHOICES
import arrow
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from base.models import BaseModel



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
class Advert(BaseModel):
    name = models.CharField(max_length=250)
    # user = models.ForeignKey(SystemUser,
    #                          on_delete=models.CASCADE)
#     Consider using a separate image class
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)

class Category(BaseModel):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=True)
    target_price = models.DecimalField(max_digits=8, decimal_places=2)
    start_price = models.DecimalField(max_digits=8, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    status = models.BooleanField(default=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)

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
        if self.start_time >= arrow.utcnow():
            return True

    def is_running(self):
        current_time = arrow.utcnow()
        if current_time >= self.start_time and current_time <= self.end_time:
            return True

    def has_ended(self):
        current_time = arrow.utcnow()
        if current_time > self.end_time:
            return True
    def time_left(self):
        if self.is_running():
            time = ''
            diff = self.end_time - arrow.utcnow()
            days = diff.day
            hours = diff.hour
            minutes = diff.minute
            seconds = diff.second

            if days:
                time += '{} days'.format(days)
            if hours:
                time += '{} hours'.format(hours)
            if minutes:
                time += '{} minutes'.format(minutes)
            if seconds:
                time += '{} seconds'.format(seconds)
            return time
        else:
            return 'ended'


    def get_current_price(self):
        bids = Bid.objects.filter(event=self).order_by('-amount')
        count = bids.count()

        if count:
            return bids[0].amount
        else:
            return self.start_price

    def winner(self):
        bids = Bid.objects.filter(event=self)
        count = bids.count()

        if self.has_ended():
            if count == 0:
                return "No one placed a bid on this item"
            elif count == 1:
                return bids[0].bidder
            else:
                winner = bids.order_by('-amount')[0].bidder
        else:
            return "No Winner yet"








    def __str__(self):
        return self.item











class Bid(BaseModel):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    bidder = models.ForeignKey(User,
                                on_delete=models.CASCADE, null=True, related_name='bids')
    event = models.ForeignKey(AuctionEvent,
                              on_delete=models.CASCADE, null=True, related_name='bids')
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ('-created_at',)



     # Takes an argument and returns the current bid object
    # The current bid must be higher than the highest bid so far









class Ratings(models.Model):
    pass


