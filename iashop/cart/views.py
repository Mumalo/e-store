from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from auction.models import AuctionEvent, WatchList
from .cart import Cart

@require_POST
def add_to_watch_list(request):

    id = int(request.POST.get('id'))
    action = request.POST.get('action')
    list = {}

    if id and action:
        # cart = Cart(request)
        try:
            auction = AuctionEvent.objects.get(id=id)
            user = request.user

            if action == 'watch':
                w = WatchList(creator=user)
                w.save()
                if auction not in w.items.all():
                    w.items.add(auction)
            else:
                WatchList.objects.filter(creator=request.user, items=auction).delete()
            return JsonResponse({'status':'ok','id':id})
        except ObjectDoesNotExist:
            return JsonResponse({'status':'ko'})
    else:
        return JsonResponse({'status':'ko'})


# add to cart view in the future that uses sessions to store cart data