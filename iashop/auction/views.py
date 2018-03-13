from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from .forms import AuctionForm, BidForm, AdvancedSearchForm, AdvertForm, BudgetForm, EmailPostForm, GeneralSearchForm, ImageForm
# from .models import Buyer, Seller
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory, modelform_factory
from .models import AuctionEvent, Bid, Category, Advert, BudgetPlan, SubCategory, SubCategory2
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import get_user
from .models import User
from django.views.generic.edit import DeleteView
from django.http import JsonResponse
import json
from django.core import serializers
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
# from django.core.mail import send_mail, BadHeaderError
from  django.template import RequestContext
from common.decorators import ajax_required
from notifications.signals import notify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
@description: for a given Sub category selected
populate next drop down with items
belonging to that sub category
:param request
:rtype json

"""
@ajax_required
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
            items[sub_category] = [serializers.serialize("json", SubCategory2.objects.filter(sub_category__name=sub_category))]

    # subs = SubCategory.objects.filter(category=data)

    return JsonResponse(items, safe=False)

"""
@description: for a given category selected
populate next drop down with items
belonging to that category
:param request
:rtype json

"""
@ajax_required
@login_required
def select_by_category(request):
    submitted_cat = request.POST.get('category')
    result_set = []
    # data = None

    if submitted_cat:
        try:
            cat = Category.objects.get(name=submitted_cat)
            for s in cat.subcat.all():
                result_set.append(str(s.name))
            # data = serializers.serialize("json", detail.html(cat.subcat.all()))
        except:
            pass

    return JsonResponse(result_set, safe=False)
@login_required
@ajax_required

def select_by_subcat(request):
    subcat = request.POST.get('subcat')
    result = []

    if subcat:
        try:
            sub = SubCategory.objects.get(name=subcat)
            for s in sub.subcat2.all():
                result.append(str(s.name))
        except:
            pass
    return JsonResponse(result, safe=False)
    ''

"""
Mark all notifications as read
for a particular recipient
"""
@login_required
@ajax_required
def mark_all_as_read(request):

    action = request.POST.get('recipient')
    user = None
    nfs = None
    if action:
        try:
            user = User.objects.get(username=action)
            unread = user.notifications.unread()
            unread.mark_all_as_read()
        except ObjectDoesNotExist:
            return JsonResponse({'status':'ko'})

        return JsonResponse({'status':'ok'})
    return JsonResponse({'status':'ko'})

"""
Mark a particular notification as read
for a given recipient
"""
@login_required
@ajax_required
def mark(request):
    id = request.POST.get('id')
    user = request.user

    if id and user:
        try:
            notification = user.notifications.filter(id=id)
            notification.mark_all_as_read()
            return JsonResponse({'status':'ok'})
        except ObjectDoesNotExist:
            return JsonResponse({'status':'ko'})
    return JsonResponse({'status':'ko'})

"""
Show all categories belonging to the system
"""
def all_categories(request):
    categories = Category.objects.all()
    items = AuctionEvent.objects.all()

    return render(request,"auction/category/category_list.html",
                  {'categories':categories, 'items':items})

"""
example slug shoes
slug is a string identifier for a category
category detail page shows all items belinging to it
:param category_id:
:param category_slug

"""
def category_detail(request, category_id, category_slug):

    category = None
    items = None
    sub_category = None
    try:
        category = Category.objects.get(id=category_id, slug=category_slug)
        items = AuctionEvent.objects.filter(category=category)
    except ObjectDoesNotExist:
        pass

    return render(request, "auction/category/category_detail.html",
                  {'category': category, 'items': items,})


def subcat_detail(request, subcat_id=None, subcat_slug=None):

    subcat = None
    items = None
    subcat2 = None
    try:
        subcat = SubCategory.objects.get(id=subcat_id, slug=subcat_slug)
        items = AuctionEvent.objects.filter(sub_category=subcat)
    except ObjectDoesNotExist:
        pass
    return render(request, "auction/subcategory/detail.html", {'subcat':subcat, 'items':items})


"""
subcat2 represents a category under a subcategory
Example: Category = Automobiles, subcategory = cars
subcat2 = BMW

"""
def subcat2_detail(request, subcat_id=None, subcat_slug=None):

    subcat2 = None
    try:
        subcat2 = SubCategory2.objects.get(id=subcat_id, slug=subcat_slug)
    except ObjectDoesNotExist:
        pass
    return render(request, "auction/subcategory/subcat2-detail.html", {'subcat2':subcat2})


"""
subcategory and subcateory2 are autopopulated
when adding a new item
An item can have many photos
"""
@login_required
def add_new_auction(request):

    ImageFormset = formset_factory(ImageForm, can_delete=True)
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        formset = ImageFormset(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            photos = []
            cleaned_sub = form.cleaned_data.get('sub_category3')
            cleaned_sub2 = form.cleaned_data.get('sub_category4')
            sub_cat = None
            sub_cat2 = None
            new_form = form.save(commit=False)
            current_user = get_user(request)
            new_form.creator = current_user
            images = []
            """
            Save corresponding subcategories item belongs to
            if they exist
            """
            if cleaned_sub:
                try:
                    sub_cat = SubCategory.objects.get(name=cleaned_sub)
                except ObjectDoesNotExist:
                    pass
            if cleaned_sub2:
                try:
                    sub_cat2 = SubCategory2.objects.get(name=cleaned_sub2)
                except ObjectDoesNotExist:
                    pass

            new_form.sub_category = sub_cat
            new_form.sub_category2 = sub_cat2
            form.save()
            for form in formset:
                image = form.save()
                new_form.image.add(image)

            """
            Send a notification to all users that this item has been added
            except the current user
            """
            users = User.objects.exclude(id=current_user.id)
            users = list(users)
            auction = new_form
            notify.send(current_user, recipient=users, verb='created a new item', target=auction)

            return  render(request, 'auction/auction_complete.html')
    else:
        """
        if form validation falied
        render an empty form and
        stay on the same page
        """
        form = AuctionForm()
        formset = ImageFormset()
    return render(request, 'auction/new_auction.html',
                  {'form': form, 'formset':formset}, )

# ajax view to select by category
"""
custom comtext processor to
render search forms and all items
in the items index page
"""
def custom_processor(request):

    all_auctions_list  = AuctionEvent.objects.all()
    paginator = Paginator(all_auctions_list, 10)
    page = request.GET.get('page')
    try:
        auctions = paginator.page(page)
    except PageNotAnInteger:
        auctions = paginator.page(1)
    except EmptyPage:
        auctions = paginator.page(paginator.num_pages)

    for auction in all_auctions_list:
        if auction.has_ended():
            auction.available = False
            auction.save()
    search_form = AdvancedSearchForm()
    # available_auctions = AuctionEvent.objects.filter(available=True)

    return {
        'app': 'auction',
        'search_form':search_form,
         'auctions':auctions,
    }

"""
displays list of all items in the system
paginated by n items a page
n = 10 in this case
"""
def auction_list(request):
    categories = Category.objects.all()
    # Edit this line of code later

    # match = None

    if "g_search" in request.GET:
        general_search = GeneralSearchForm(data=request.GET)


        if general_search.is_valid():
            """
            if the user made a search
            show only items belinging to that search query
            """
            g_search_list = general_search.search()
            number = g_search_list.count()
            paginator = Paginator(g_search_list, 10)
            page = request.GET.get('page')
            try:
                g_search = paginator.page(page)
            except PageNotAnInteger:
                g_search = paginator.page(1)
            except EmptyPage:
                g_search = paginator.page(paginator.num_pages)

            cat = general_search.category()
            return render_to_response('auction/list.html', {'g_search':g_search, 'gs_number':number}, context_instance=RequestContext(request, processors=[custom_processor]))

    if "sub_search" in request.GET:
        """
        this can be side bar search seen on the actions list page
        show only items belonging to this search a search was
        made in this form
        """
        search_form = AdvancedSearchForm(data=request.GET)
        if search_form.is_valid():
            search_list = search_form.search()
            number = search_list.count()
            page = request.GET.get('page')
            paginator = Paginator(search_list, 10)
            try:
                search = paginator.page(page)
            except PageNotAnInteger:
                search = paginator.page(1)
            except EmptyPage:
                search = paginator.page(paginator.num_pages)

            return render_to_response('auction/list.html', {'search':search, 's_number':number}, context_instance=RequestContext(request, processors=[custom_processor]))
    else:
        g_search = None
        search = None
        cat = None
    return render_to_response('auction/list.html', context_instance=RequestContext(request, processors=[custom_processor]))

"""
:param request:
:param: auction_id
"""
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
        edit_form = AuctionForm(data=None, instance=auction)
    return render(request, 'auction/edit_auction.html', {'edit_form': edit_form})


@login_required
def auction_detail(request, auction_id):
    auction = get_object_or_404(AuctionEvent, id=auction_id)
    sent = False
    if request.method == 'POST':
        bid_form = BidForm(data=request.POST, auction=auction, bidder=request.user)
        private_message = EmailPostForm(data=request.POST)
        sender = request.user

        try:
            creator = AuctionEvent.objects.get(id=auction_id).creator
        except:
            creator = None

        if private_message.is_valid():
            """
            form to send private messages to owner of this item
            """
            message = private_message.cleaned_data.get('message')

            if creator and sender and message:
                from_email = settings.EMAIL_HOST_USER
                to_email = creator.email
                subject = "{}, {} is interested in {}".format(sender, sender.email, auction.item)
                message = "{}".format(message)
                """
                send message from user with from_email
                to user with to_email
                """
                private_message.send(subject, message, from_email, [to_email])

        if bid_form.is_valid():
            """
            save if there was a bid on the item
            """
            bidder = get_user(request)
            bid_form.save(commit=False)

            if auction.creator == bidder:
                """
                the owner of the item cannot bid on this
                """
                messages.error(request, 'You cannot Bid on your own item')
            elif auction.creator != bidder:
                users = User.objects.filter(id=auction.creator.id)

                messages.success(request, 'Your Bid was submitted')
        else:
            messages.error(request, 'error')

    else:
        bid_form = BidForm(auction=auction, bidder=request.user)
        private_message = EmailPostForm()
    return render(request, 'auction/auction_detail.html',
                  {'bid_form': bid_form,
                   'auction': auction,
                   'private_message':private_message,
                   'sent': sent})


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
        budget_form = BudgetForm(data=request.POST, files=request.FILES)
        if budget_form.is_valid():
            new_budget = budget_form.save(commit=False)
            new_budget.creator = request.user
            current_user = get_user(request)
            new_budget.available = True

            users = User.objects.exclude(id=current_user.id)
            users = list(users)
            notify.send(current_user, recipient=users, verb='added a new budget plan', target=new_budget)

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

        if budget_form.is_valid() and request.user.id == creator.id:
            new_budget = budget_form.save(commit=False)
            new_budget.creator = creator
            new_budget.available = True
            new_budget.save()
            messages.success(request, 'budget updated successfully')
    else:
        budget_form = BudgetForm(instance=budget)
    return render(request, 'auction/advert/budget_edit.html', {'budget_form':budget_form})


"""
Json delete view for budget plan and auction
"""
@login_required
@ajax_required
def delete_view(request):

    id = request.POST.get('id', None)
    confirm_delete = request.POST.get('confirm', None)
    action = request.POST.get('action', None)

    if id:
        if action == 'budget':
            try:
                budget = BudgetPlan.objects.get(id=id)

                if confirm_delete and confirm_delete == 'true':
                    budget.delete()
                    return JsonResponse({'status':'ok'})
                # budget.delete()

            except ObjectDoesNotExist:
                return JsonResponse({'status':'ko'})
        if action == 'item':
            try:
                item = AuctionEvent.objects.get(id=id)

                if confirm_delete and confirm_delete == 'true':
                    item.delete()
                    return JsonResponse({'status':'ok'})
                # budget.delete()

            except ObjectDoesNotExist:
                return JsonResponse({'status':'ko'})

    else:
        return JsonResponse({'status':'ko'})



# Views for creating budget plan


# Use Generic views for deleting objects






# Create your views here.


# Create your views here.
