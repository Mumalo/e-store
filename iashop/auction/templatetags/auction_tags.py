import datetime, time
import arrow
from django import template
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from ..models import AuctionEvent, Bid, Category, SubCategory, WatchList, ItemOfTheDay, BudgetPlan
from ..forms import EmailPostForm
from django.db.models import Count
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.template import Context
# from cart.cart import Cart
from ..forms import GeneralSearchForm

register = template.Library()

@register.filter(name='to_json')
def to_json(t):
    if isinstance(t, datetime.datetime):
        return '{}'.format(int(time.mktime(t.timetuple()))*1000)
    else:
        return 'Wrong format'


@register.inclusion_tag(file_name="auction/tags/search.html", takes_context=True)
def search_form(context):
    # request = context["request"]
    form = GeneralSearchForm()


    # if request.method == 'GET':
    #     form = GeneralSearchForm(data=request.GET)
    #
    #     if form.is_valid():
    #         search = form.search()
    # else:
    #     form = GeneralSearchForm()
    #     search = None
    #     cat = None
    return {'form':form}

@register.inclusion_tag(file_name='auction/tags/product_list.html', takes_context=True)
def product_list(context, items):

    if items is not None:
        request = context['request']
        user = request.user
        watch_list = None
        owner = None

        if not user.is_anonymous():
            watch_list = WatchList.objects.filter(creator=user)

        watching = []

        if watch_list is not None:
            for list in watch_list:
                for item in list.items.all():
                    watching.append(item)
            owner = [list.creator for list in watch_list][:1]


        return {'request':request,'items':items,'owner':owner, 'watch_list':watching}


# @register.assignment_tag(takes_context=True)
# def search_results(context):
#     request = context["request"]
#
#
#     if register.method == 'GET':
#         search = GeneralSearchForm(data=register.GET).search()
#
#
#     else:
#         search = None
#
#     return {'search_result':search}
#
#








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
    hottest_list = []
    if user is not None:
        auctions = AuctionEvent.objects.filter(available=True, creator=user)
    hottest = auctions.annotate(total_bids=Count('bids')).order_by('-total_bids')[:count]
    hottest_list = [a for a in hottest if a.is_running()]
    return hottest_list[:count]


@register.assignment_tag
def latest_auctions(user=None, count=5):
    auctions = AuctionEvent.objects.filter(available=True)
    if user is not None:
        auctions = AuctionEvent.objects.filter(available=True, creator=user)
    return auctions.order_by('-time')[:count]

@register.assignment_tag
def best_offers(auction=None):
    bids = None
    if auction is not None:
        bids = Bid.objects.filter(event=auction).order_by('-amount')[:3]

    return bids



@register.assignment_tag
def ending_soon(user=None, count=10):
    ending_soon_list = []
    auctions = AuctionEvent.objects.filter(available=True)
    if user is not None:
        auctions = AuctionEvent.objects.filter(available=True, creator=user)
    for a in auctions:
        if a.place_on_auction:
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

@register.assignment_tag()

def wond_bids(user=None):

    bids = {}
    won = []
    lost = []



    if user is not None:
        auctions = AuctionEvent.objects.filter(available=True)
        bidders = [ bid.bidder for bid in Bid.objects.filter(bidder=user)]

        for a in auctions:
            if a.winner == user and user in bids:
                won.append(a)
                bids['won'] = won
            elif a.has_ended() and a.winner != user and user in bidders:
                lost.append(a)
                bids['lost'] = lost
    return bids

@register.assignment_tag
def watch_list(user=None):

    list = None
    if user is not None:
        list = WatchList.objects.filter(creator=user)
    return list



@register.assignment_tag
def item_of_the_day(count=10):

    for i in ItemOfTheDay.objects.all():

        if i.category:
            return i.category.cat_products.all()[:count]
        elif i.subcategory:
            return i.subcategory.sub_products.all()[:count]
        elif i.user:
            return AuctionEvent.objects.filter(creator=i.user)[:count]


@register.assignment_tag(takes_context=True)
def budget_plan(context, user=None):
    request = context["request"]

    if user:
        budget = BudgetPlan.objects.filter(creator=user)
    return budget


# @register.inclusion_tag(file_name="auction/tags/budget_reply.html",takes_context=True)
# def satisfy_budget(context, user, b):
#     request = context["request"]
#     budget_reply =  EmailPostForm()
#     return {'request':request, 'budget_reply':budget_reply, 'user':user}
















