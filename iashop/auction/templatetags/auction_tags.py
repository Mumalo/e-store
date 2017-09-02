import datetime, time
import arrow
from django import template
from ..models import AuctionEvent, Bid, Category, SubCategory
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist


register = template.Library()

@register.filter(name='to_json')
def to_json(t):
    if isinstance(t, datetime.datetime):
        return '{}'.format(int(time.mktime(t.timetuple()))*1000)
    else:
        return 'Wrong format'



# return total auctions for a particular user or general if user object is not passed

@register.simple_tag
def total_auctions(user=None):

    if user is not None:
        return AuctionEvent.objects.filter(available=True, creator=user).count()
    else:
        return AuctionEvent.objects.filter(available=True).count()

@register.assignment_tag
def product_categories(count=10):
    return Category.objects.all()[:count]

@register.assignment_tag
def auctions_in_category(category=None):
    return AuctionEvent.objects.filter(category=category)


@register.assignment_tag
def live_auctions(user=None, count=10):
    live_list = []
    auctions = AuctionEvent.objects.filter(available=True)
    if user is not None:
        auctions = AuctionEvent.objects.filter(available=True,creator=user)
    for a in auctions:
        if a.is_running():
            live_list.append(a)
    return live_list[:count]

@register.assignment_tag
def hottest_deals(user=None, count=5):
    auctions = AuctionEvent.objects.filter(available=True)
    list = []
    if user is not None:
        auctions = AuctionEvent.objects.filter(available=True, creator=user)
    return auctions.annotate(total_bids=Count('bids')).order_by('-total_bids')[:count]


@register.assignment_tag
def latest_auctions(user=None, count=5):
    auctions = AuctionEvent.objects.filter(available=True)
    if user is not None:
        auctions = AuctionEvent.objects.filter(available=True, creator=user)
    return auctions.order_by('-time')[:count]



@register.assignment_tag
def ending_soon(user=None, count=10):
    ending_soon_list = []
    auctions = AuctionEvent.objects.filter(available=True)
    if user is not None:
        auctions = AuctionEvent.objects.filter(available=True, creator=user)
    for a in auctions:
        now = datetime.datetime.now()
        diff = a.end_time - arrow.utcnow()
        if diff.days == 0:
            ending_soon_list.append(a)
    return ending_soon_list

@register.assignment_tag
def ended_auctions(user=None):
    ended_list = []
    if user is not None:
        for a in AuctionEvent.objects.filter(available=True, creator=user):
            if a.has_ended:
                ended_list.append(a)
    return ended_list


# @register.inclusion_tag('auction/sub_cat_for_cat.html', takes_context=True)
# def sub_cats_for_cats(context):
#     request = context['request']
#     category = request.POST.get('category')
#     return {'category': category}

















