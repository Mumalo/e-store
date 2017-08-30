from django.shortcuts import render, get_object_or_404, HttpResponse
from .forms import AuctionForm, BidForm, AdvancedSearchForm, AdvertForm, BudgetForm
# from .models import Buyer, Seller
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from .models import AuctionEvent, Bid, Category, Advert, BudgetPlan, SubCategory
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user
from .models import User
from django.views.generic.edit import DeleteView
from django.http import JsonResponse
import json
from django.core import serializers
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

def sub_cats_for_cats(request):
    data = request.POST.get('cat')
    new_data = None
    sub = []
    items = {}

    if data:
        new_data = data
        subs = SubCategory.objects.filter(category__name=new_data)
        for s in subs:
            sub_category = str(s)
            items[sub_category] = [str(item) for item in AuctionEvent.objects.filter(sub_category__name=sub_category)]

    # subs = SubCategory.objects.filter(category=data)

    return JsonResponse(items, safe=False)

def select_by_category(request):
    submitted_cat = request.POST.get('category')
    result_set = []
    # data = None

    if submitted_cat:
        try:
            cat = Category.objects.get(name=submitted_cat)
            for s in cat.subcat.all():
                result_set.append(str(s.name))
            # data = serializers.serialize("json", list(cat.subcat.all()))
        except:
            pass

    return JsonResponse(result_set, safe=False)


def home(request):
    return render(request, 'home.html')

@login_required
def add_new_auction(request):

    if request.method == 'POST':
        form = AuctionForm(request,request.POST, request.FILES)

        if form.is_valid():
            cleaned_sub = form.cleaned_data.get('sub_category2')

            new_form = form.save(commit=False)
            current_user = get_user(request)
            new_form.creator = current_user

            if cleaned_sub:
                sub_cat = SubCategory.objects.filter(name=cleaned_sub)[0]
            else:
                sub_cat = None

            new_form.sub_category = sub_cat




            new_form.save()

            return render(request, 'auction/auction_complete.html')
    else:
        form = AuctionForm(request)
    return render(request, 'auction/new_auction.html',
                  {'form': form}, )

# ajax view to select by category



def auction_list(request):
    categories = Category.objects.all()
    # Edit this line of code later
    auctions = AuctionEvent.objects.filter(available=True)
    match = None

    if request.method == 'POST':
        search_form = AdvancedSearchForm(data=request.POST)
        if search_form.is_valid():
            match = search_form.search()
    else:
        search_form = AdvancedSearchForm()


    return render(request, 'auction/list.html',
                  {'auctions': auctions, 'search_form': search_form, 'match': match, 'categories': categories, })

@login_required
def edit_auction(request, auction_id):

    auction = get_object_or_404(AuctionEvent, id=auction_id)
    creator = auction.creator
    if request.method == 'POST':
        edit_form = AuctionForm(data=request.POST, instance=auction)

        if edit_form.is_valid():
            new_auction = edit_form.save(commit=False)
            new_auction.creator = creator
            new_auction.save()
            return messages.success(request, 'auction updated successfully')
    else:
        edit_form = AuctionForm(instance=auction)
    return render(request, 'auction/edit_auction.html', {'edit_form': edit_form})

def auction_detail(request, auction_id):
    auction = get_object_or_404(AuctionEvent, id=auction_id)

    if request.method == 'POST':
        bid_form = BidForm(data=request.POST, auction=auction, bidder=request.user)
        if bid_form.is_valid():
            bid = bid_form.save()
            # return render(request, 'auction/bid_confirm.html', {'auction':auction})
            messages.success(request, 'Your Bid was submitted')
        else:
            messages.error(request, 'error')
    else:
        bid_form = BidForm(auction=auction, bidder=request.user)



    return render(request, 'auction/auction_detail.html',
                  {'bid_form':bid_form,
                   'auction': auction,})

@login_required
def create_advert(request):

    if request.method == 'POST':
        advert_form = AdvertForm(request.POST)

        if advert_form.is_valid():
            new_advert = advert_form.save(commit=False)
            new_advert.creator = request.user
            new_advert.save()
            return  messages.success(request, 'Advert added successfully')
    else:
        advert_form = AdvertForm()
    return render(request, 'auction/advert/new_advert.html')

@login_required
def post_advert(request, advert_id):
    advert = get_object_or_404(Advert, pk=advert_id)
    advert.available = True


def advert_list(request):
    adverts = Advert.objects.filter(available=True)

    return render(request, 'auction/adverts.html', {'adverts', adverts})






@login_required
def edit_advert(request, pk):

    advert = get_object_or_404(Advert, pk=pk)
    creator = advert.creator
    if request.method == 'POST':
        advert_form = AdvertForm(data=request.POST, instance=advert)
        if advert_form.is_valid() and request.user.id == creator.id:
            advert_form.creator = request.user
            advert_form.save()
    else:
        advert_form = AdvertForm(instance=Advert)
    return render(request, 'auction/edit_advert.html', {'advert_form': advert_form, 'creator':creator})

class AdvertDelete(DeleteView):
    model = Advert
    success_url = reverse_lazy('account:user_detail')


@login_required
def create_budget_plan(request):
    if request.method == 'POST':
        budget_form = BudgetForm(data=request.POST)
        if budget_form.is_valid():
            new_budget = budget_form.save(commit=False)
            new_budget.creator = request.user
            new_budget.available = True
            new_budget.save()
            messages.success(request, 'budget added successfully')
    else:
        budget_form = BudgetForm()
    return render(request, 'auction/advert/new_budget.html', {'budget_form': budget_form})

@login_required
def update_budget(request, budget_id):

    budget = get_object_or_404(BudgetPlan, id=budget_id)
    creator = budget.creator

    if request.method == 'POST':
        budget_form = BudgetForm(data=request.POST, instance=budget)

        if budget.is_valid() and request.user.id == creator.id:
            new_budget = budget_form.save(commit=False)
            new_budget.creator = creator
            new_budget.available = True
            new_budget.save()
    else:
        budget_form = BudgetForm(instance=budget)
    return render(request, 'auction/advert/budget_adit.html')

class BudgetDelete(DeleteView):
    model = BudgetPlan
    success_url = reverse_lazy('account:user_detail')

# Views for creating budget plan


# Use Generic views for deleting objects






# Create your views here.


# Create your views here.
