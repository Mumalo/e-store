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
from django.core.exceptions import ValidationError
from photologue.models import Photo, ImageModel


class Category(BaseModel):
    name = models.CharField(max_length=250, unique=True, null=True, db_index=False)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250, null=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d',blank=True, null=True)

    # return all subcategories under this category
    def custom_queryset(self):
        return self.subcategory.all()

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    name = models.CharField(max_length=250,  unique=True, null=True)
    slug = models.SlugField(max_length=250, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,related_name='subcat')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub Categories'


class SubCategory2(BaseModel):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, related_name='subcat2')

    class Meta:
        verbose_name_plural = 'Sub Categories 2'

    def __str__(self):
        return self.name


class Image(ImageModel):
    pass


class AuctionEvent(BaseModel):
    item = models.CharField(max_length=125, blank=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=True, related_name='cat_products')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True, related_name='sub_products')
    sub_category2 = models.ForeignKey(SubCategory2, on_delete=models.CASCADE, blank=True, null=True, related_name='sub_products2')
    # sub_category = ChainedForeignKey(
    #     SubCategory,
    #     chained_field='category',
    #     chained_model_field='category',
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True,
    # )
    target_price = models.DecimalField(max_digits=50, decimal_places=2)
    start_price = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    current_price = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE, null=True)
    # image = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    image = models.ManyToManyField(Image, blank=True)
    time = models.DateTimeField(default=timezone.now)
    available = models.BooleanField(default=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    place_on_auction = models.NullBooleanField(default=True, help_text='if you click this you must provide start time, end time, start price and target price')

    class Meta:
        ordering = ('-time',)

    def clean(self):
        auction_start_time = arrow.get(self.start_time)
        auction_end_time = arrow.get(self.end_time)
        auction_start_price = self.start_price

        if self.place_on_auction:
            if auction_start_time < arrow.utcnow() or auction_end_time < arrow.utcnow():
                raise ValidationError('Auction cannot be created in the past')
            if auction_end_time < auction_start_time:
                raise ValidationError('End time cannot be less than start time')
            if auction_start_time > auction_end_time:
                raise ValidationError('Start time cannot be greater than end time')

    def has_started(self):

        if self.place_on_auction:
            started = self.start_time >= arrow.utcnow()

            if started:
                return True
            else:
                self.available = False
                return False
        else:
            return True

    def has_ended(self):
        if self.place_on_auction:
            current_time = arrow.utcnow()
            ended = current_time > self.end_time
            if ended:
                self.available = False
                return True
        else:
            return False

    def is_running(self):

        if self.place_on_auction:
            return self.has_started() and not self.has_ended()
        else:
            return True

    def time_left(self):

        if self.place_on_auction:
            if self.is_running():
                diff = self.end_time - arrow.utcnow()
                return diff.day
            else:
                return 'ended'

    def get_current_price(self):

        if self.place_on_auction:
            bids = Bid.objects.filter(event=self).order_by('-amount')
            count = bids.count()

            if count:
                current_price =  bids[0].amount
                return bids[0].amount
            else:
                if self.start_price:
                    return self.start_price
        else:
            return self.target_price

    def total_bids(self):

        if self.place_on_auction:
            return Bid.objects.filter(event=self).count()

    def winner(self):

        if self.place_on_auction:
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

    def is_available(self):
        if self.has_ended() or not self.has_started():
            self.available = False


class WatchList(BaseModel):

    creator = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(AuctionEvent)


class Bid(BaseModel):
    BID_AMOUNT_CHOICES = (
        (500, '500.00'),
        (1000, '100.00'),
    )
    amount = models.IntegerField(choices=BID_AMOUNT_CHOICES, blank=True, null=False)
    bidder = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='bidder')
    event = models.ForeignKey(AuctionEvent,on_delete=models.CASCADE, null=True, related_name='bids')
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ('-created_at',)


class Advert(BaseModel):
    title = models.CharField(max_length=250, null=True)
    image = models.ImageField(blank=False, null=True,upload_to='advert/%Y/%m/%d')
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='advert')
    available = models.BooleanField(default=False)


    class Meta:
        ordering = ('-last_created', )

    def __str__(self):
        return self.title


class BudgetPlan(Advert):
    range = models.IntegerField(null=True)
    TIME_CHOICES = (
        ('YEARS','Years'),
        ('MONTHS','Months'),
        ('WEEKS','Weeks'),
        ('DAYS','Days'),
        ('HOURS','Hours'),
        ('MINUTES','Minutes'),
        ('SECONDS', 'Seconds'),
    )
    time = models.CharField(choices=TIME_CHOICES, max_length=75, null=True)


class Ratings(models.Model):
    time_frame = models.CharField(max_length=125, null=True)


class ItemOfTheDay(BaseModel):
    category = models.ForeignKey(Category, blank=True, null=True, help_text='Please select a category to include')
    user = models.ForeignKey(User, blank=True, null=True, help_text='Please select a user whose items you wish to include')
    subcategory = models.ForeignKey(SubCategory, blank=True, null=True, help_text='Please select select a sub category to include')

    def clean(self):
        c = self.category
        u = self.user
        s = self.subcategory

        if (c and u and s) or (c and u) or (c and s) or (u and s):
            raise ValidationError('Please select one option')

    class Meta:
        verbose_name = 'Item of the day'
        verbose_name_plural = 'Items of the day'



