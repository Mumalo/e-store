from decimal import Decimal

# from material.frontend.forms import
import arrow
from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.forms import ModelForm, Textarea
from django.shortcuts import HttpResponse
from material import Layout, Fieldset, Row

from .models import AuctionEvent, Bid, Advert, BudgetPlan, Category, Image


# def get_item_label(self, item):
    #     return "{}, {}".format(item.name, item.category)

     # def get_item_label(self, item):
     #     return "{}, {}" .format (item.name, item.category)


class EmailPostForm(forms.Form):
    message = forms.CharField(widget=Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(EmailPostForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'class': 'browser-default'})
        self.layout = Layout(
            Fieldset('',
                     'message')
        )

    def send(self, subject, message, from_email, to_email):
        sent = False

        try:
            send_mail(subject, message, from_email, to_email)
            sent = True
        except BadHeaderError:
            return HttpResponse('Invalid Header found')
        ''


class GeneralSearchForm(forms.Form):
    first_choice = ('All','All')
    CHOICES = [(c.id, str(c.name)) for c in Category.objects.all()]
    CHOICES.insert(0, (None, 'All'))
    s_key = forms.CharField(required=False, max_length=240)
    in_category = forms.ChoiceField(required=False, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(GeneralSearchForm, self).__init__(*args, **kwargs)
        self.fields['s_key'].widget.attrs.update({'class':'search-key'})
        self.fields['in_category'].widget.attrs.update({'class': 'browser-default', 'id':'in_category_field'})

        

    def search(self):
        cleaned_key = self.cleaned_data.get('s_key')
        cleaned_in_cat = self.cleaned_data.get('in_category')
        search = None

        if cleaned_key and not cleaned_in_cat:
            search = AuctionEvent.objects.filter(available=True, item__icontains=cleaned_key)
            # search = 'Me'

        if cleaned_key and cleaned_in_cat:
            search = AuctionEvent.objects.filter(available=True, category__id=cleaned_in_cat, item__icontains=cleaned_key)

        return search

    def category(self):
        cat =  self.cleaned_data.get('in_category')
        return cat







class AuctionForm(ModelForm):
    sub_category3 = forms.CharField(max_length=250, widget=forms.Select, required=False)
    sub_category4 = forms.CharField(max_length=250, widget=forms.Select, required=False)

    def __init__(self, *args, **kwargs):
        super(AuctionForm, self).__init__(*args, **kwargs)
        # self.fields['sub_category2'].queryset = SubCategory.objects.none()
        self.fields['category'].widget.attrs.update({'id':'cat-select','class': 'browser-default'})
        self.fields['description'].widget.attrs.update({'class':'description', })
        self.fields['sub_category3'].widget.attrs.update({'id':'sub-cat-select','class': 'browser-default'})
        self.fields['sub_category3'].label = 'Sub Category'
        self.fields['sub_category4'].widget.attrs.update({'id':'sub-cat-select2','class': 'browser-default'})
        self.fields['sub_category4'].label = 'Sub Category 2'
        self.fields['place_on_auction'].widget.attrs.update({'id':'auction'})
        self.fields['start_time'].widget.attrs.update({'id':'start_time'})
        self.fields['start_time'].required = False
        self.fields['end_time'].widget.attrs.update({'id':'end_time'})
        self.fields['end_time'].required = False
        self.fields['start_price'].widget.attrs.update({'id':'start_price'})
        self.fields['start_price'].required = False


        self.layout = Layout(
            Fieldset(
                'Auction Information',
                Row('item'),
                Row('category', 'sub_category3' ,'sub_category4'),
                Row('place_on_auction'),
                Row('start_time', 'end_time'),
                Row('target_price', 'start_price'),
                    'available',
                    'description',
            ),
        )


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
        fields = ['item', 'category', 'sub_category' ,'sub_category2' ,'target_price', 'start_price', 'start_time', 'end_time', 'available', 'description', 'place_on_auction']
        exclude = ['subcategory','image',]
        # widgets = {
        #     'sub_category': autocomplete.ModelSelect2(url='auctions:subcategory-autocomplete', forward=['category'])
        # }

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image',]

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.layout = Layout(
            Fieldset(
                "",
                'image'
            ),
        )

# class BaseImageFormSet(forms.BaseForm):
#     def add_fields(self, form, index):
#         super(BaseImageFormSet, self).add_fields(form, index)
#         form.fields["DELETE"] = forms.BooleanField()

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
        if event_end_time and now > event_end_time:
            raise ValidationError('This Auction has ended')




    def save(self ,commit=True):
        bid = super(BidForm, self).save(commit=False)

        if self.bidder != self.event.creator:
            bid.event = self.event
            bid.bidder = self.bidder
            bid.save()



    class Meta:
        model = Bid
        fields = ['amount']

class AdvancedSearchForm(forms.Form):
    key = forms.CharField(max_length=200, required=False)
    max = forms.DecimalField(decimal_places=2, max_digits=8, required=False)
    min = forms.DecimalField(decimal_places=2, max_digits=8, required=False)


    def __init__(self, *args, **kwargs):

        self.layout = Layout(
            Fieldset('',
                     'key',
                     Row('min', 'max'))
        )

        super(AdvancedSearchForm, self).__init__(*args, **kwargs)




    def search(self):
        cleaned_key = self.cleaned_data.get('key')
        cleaned_max = self.cleaned_data.get('max')
        cleaned_min = self.cleaned_data.get('min')
        # current_price = AuctionEvent.get_current_price
        search_r=None

        if cleaned_key:
            search_r = AuctionEvent.objects.filter(available=True, item__icontains=cleaned_key)

        elif cleaned_max:
            search_r = AuctionEvent.objects.filter(available=True, current_price__lte=cleaned_max)

        elif cleaned_min:
            search_r = AuctionEvent.objects.filter(available=True, current_price__gte=cleaned_min)

        elif cleaned_max and cleaned_min:
             search_r = AuctionEvent.objects.filter(available=True, current_price__gte=cleaned_min, current_price__lte=cleaned_max)

        elif cleaned_key and  cleaned_min:
             search_r = AuctionEvent.objects.filter(available=True, current_price__gte=cleaned_max, item__icontains=cleaned_key )

        elif cleaned_key and cleaned_max:
            search_r = AuctionEvent.objects.filter(available=True,current_price__lte=cleaned_max, item__icontains=cleaned_key)

        elif cleaned_key and cleaned_max and cleaned_min:
            search_r = AuctionEvent.objects.filter(available=True, current_price__gte=cleaned_min, current_price__lte=cleaned_max, item__icontains=cleaned_key )
        return search_r



class AdvertForm(ModelForm):

    class Meta:
        model = Advert
        fields = ['title', 'image', 'description', 'price', 'creator']

    def __init__(self, *args, **kwargs):
        super(AdvertForm, self).__init__(*args, **kwargs)
        self.layout = Layout(
            Fieldset('Place Ad Below',
                     Row('title', 'image'),
                     'price',
                     'description')
        )



class BudgetForm(ModelForm):
    # range = forms.IntegerField()
    # time = forms.ChoiceField(choices=[(str(ch), str(ch)) for ch in time_choice])


    def __init__(self, *args, **kwargs):
        super(BudgetForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'item'
        self.fields['image'].widget.attrs.update({'id': 'upload'})
        self.fields['image'].label = ''

    def clean(self):
        budgets = BudgetPlan.objects.all().count()
        if budgets > 10:
            raise ValidationError('You have reached your budget plan limit. Please edit other satisfied budgets to continue')



    class Meta:
        model = BudgetPlan
        fields = ['title', 'description', 'price' ,'time', 'range', 'image',]


# class BudgetPlanEmailForm():
#     ''
    # def save(self, commit=True):
    #     budget = super(BudgetForm, self).save(commit=False)
    #     budget.image = self.cleaned_data.get('image')
    #     budget.save()


        ''