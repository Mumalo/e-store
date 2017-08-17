from django.shortcuts import render, get_object_or_404, HttpResponse
from .forms import AuctionForm, BidForm, AdvancedSearchForm
# from .models import Buyer, Seller
from django.contrib.auth.decorators import login_required
from .models import AuctionEvent, Bid, Category
from django.contrib import messages

from django.shortcuts import render
from django.contrib.auth import get_user
from .models import User

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




# def add_bid(request):
#
#     if request.method == 'POST':
#         bid_form = BidForm(request.POST)
#
#         if bid_form.is_valid():
#             new_add_bid_form = BidForm(commit=False)
#             new_add_bid_form.creator = request.user
# #             Add this user to the seller database
#     else:
#         bid_form = BidForm()
#     return render(request, 'auction/bid', {'bid_form': bid_form})





# Create your views here.


# Create your views here.
