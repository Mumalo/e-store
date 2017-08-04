from decimal import Decimal
from .models import AuctionEvent, Advert,  Bid
from datetime import datetime
from django.core.exceptions import ValidationError

from django import forms
from django.forms import ModelForm
from material import Layout, Fieldset, Row
import arrow

# class ItemAddForm(ModelForm):
#
#
#     def __init__(self, *args, **kwargs):
#         self.layout = Layout(
#             Fieldset(
#                 'Product Informaation',
#                 Row('category', 'name'),
#                 'condition',
#                 'status'
#                 'description',
#             )
#         )
#
#         super(ItemAddForm, self).__init__(*args, **kwargs)
#
#     class Meta:
#         model = Item
#         fields = ['name', 'category', 'condition', 'status', 'description']
#         labels = {
#             'status': 'Is this item available for auction?'
#         }






class AuctionForm(ModelForm):


    def __init__(self, *args, **kwargs):
        self.layout = Layout(
            Fieldset(
                'Auction Information',
                Row('item', 'category'),
                Row('start_time', 'end_time'),
                Row('target_price', 'start_price'),
                'description',
            ),
            Fieldset(
                "Add Your Item\'s image ",
                'image'
            ),
        )
        super(AuctionForm, self).__init__(*args, **kwargs)

    def clean_start_time(self):
        start_time = self.cleaned_data.get('start_time')
        if start_time and start_time < arrow.utcnow():
            raise ValidationError('Auction cannot start in the past')
        return start_time

    def clean_end_time(self):
        end_time = self.cleaned_data.get('end_time')
        if end_time and end_time < arrow.utcnow():
            raise ValidationError('Auction cannot end in the past')
        return end_time

    def clean_start_price(self):
        target_price = self.cleaned_data.get('target_price')
        start_price = self.cleaned_data.get('start_price')

        if start_price and target_price and start_price > target_price:
            raise ValidationError('Target price must be greater than start price')
        return start_price

    def clean(self):
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')

        if start_time and end_time and start_time > end_time:
            raise ValidationError('start time cannot be greater than end time')




    class Meta:
        model = AuctionEvent
        fields = ['item', 'category', 'target_price', 'start_price', 'start_time', 'end_time', 'status', 'description', 'image']

class BidForm(ModelForm):
    def __init__(self, data=None, auction=None, bidder=None, *args, **kwargs):
        self.event = auction
        self.bidder = bidder
        super(BidForm, self).__init__(data, *args, **kwargs)

    def clean_amount(self):
        current_bid = self
        current_auction = self.event
        current_price = current_auction.get_current_price() + Decimal('0.00')
        submitted_offer = self.cleaned_data.get('amount')
        if submitted_offer:
            if submitted_offer <= current_price:
                raise ValidationError('Offer {} must be greater than current bid {}'.format(submitted_offer, current_price))


        return submitted_offer

    def clean(self):
        now = arrow.utcnow()
        event = self.event
        event_end_time = event.end_time
        if now > event_end_time:
            raise ValidationError('This Auction has ended')




    def save(self ,commit=True):
        bid = super(BidForm, self).save(commit=False)
        bid.event = self.event
        bid.bidder = self.bidder
        bid.save()



    class Meta:
        model = Bid
        fields = ['amount']