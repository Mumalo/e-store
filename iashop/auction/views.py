from django.shortcuts import render, get_object_or_404, HttpResponse
from .forms import AuctionForm, BidForm, AdvancedSearchForm, AdvertForm, BudgetForm
# from .models import Buyer, Seller
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from .models import AuctionEvent, Bid, Category, Advert, BudgetPlan
from django.contrib import messages

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user
from .models import User
from django.views.generic.edit import DeleteView

def home(request):
    return render(request, 'home.html')

login_required
def add_new_auction(request):

    if request.method == 'POST':
        form = AuctionForm(request.POST, request.FILES)

        if form.is_valid():
            new_form = form.save(commit=False)
            current_user = get_user(request)
            new_form.creator = current_user
            new_form.save()

            return render(request, 'auction/auction_complete.html')
    else:
        form = AuctionForm()
    return render(request, 'auction/new_auction.html',
                  {'form': form}, )


def auction_list(request):
    categories = Category.objects.all()
    auctions = AuctionEvent.objects.all()
    match = None

    if request.method == 'POST':
        search_form = AdvancedSearchForm(data=request.POST)
        if search_form.is_valid():
            match = search_form.search()
    else:
        search_form = AdvancedSearchForm()


    return render(request, 'auction/list.html',
                  {'auctions': auctions, 'search_form': search_form, 'match': match, 'categories': categories})

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
