from django.shortcuts import render

from decimal import Decimal
from auction.models import AuctionEvent
from django.conf import settings

# Use this module in the future for session based cart storage
class Cart(object):


    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        # if the cart is empty, save an empty cart in the session
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def show(self):
        return self.cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)

        current_bid = product.get_current_price()
        target_price = product.target_price

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                       'current_bid_at': str(current_bid),
                                       'target_price': str(target_price),}
            self.cart[product_id]['status'] = 'watching'

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

       #         Update the current session
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    # def watching(self):
    #     if 'watching' in self.cart.values():
    #         return True
    #     else:
    #         return False

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):

        product_ids = self.cart.keys()

        products =  AuctionEvent.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['target_price'] = Decimal(item['target_price'])
            item['total_price'] = item['target_price'] * item['quantity']
            yield item

        def __len__(self):

            return sum(item['quantity'] for item in self.cart.values())

        def get_total_price(self):

            return sum(Decimal(item['target_price']) * item['quantity'] for item in self.cart.values() )

        # Remove the cart from the session or clear the cart session
        def clear(self):
            del self.cart[settings.CART_SESSION_ID]
            self.session.modified = True













# Create your views here.
