

from django import template
from django.core.exceptions import ObjectDoesNotExist
from ..models import Pages


register = template.Library()


@register.assignment_tag
def social_media_links():

    page = None
    fb = None
    tw = None
    ins = None
    links = {}

    try:
        page = Pages.objects.get(title='Home')
        fb = page.fb_url
        tw = page.twitter_url
        ins = page.instagram_url

        if fb:
            links['fb'] = fb
        if tw:
            links['tw'] = tw
        if ins:
            links['ins'] = ins
        if not (fb or tw or ins):
            links = None
    except ObjectDoesNotExist:
        pass

    return links


@register.assignment_tag

def terms():
    page = None
    terms = None
    try:
        page = Pages.objects.get(title='Home')
        terms = page.text
    except ObjectDoesNotExist:
        pass
    return terms