from django.shortcuts import render


from django.shortcuts import render
from .models import Pages
from django.core.exceptions import ObjectDoesNotExist



def home(request):

    p = None
    images = None
    terms = None

    try:
        p = Pages.objects.get(title='Home')
        # images = [i for i in p.gallery.photos.all()]
        images = p.photos.all()
        text = p.text
    except ObjectDoesNotExist:
        p = None

    return render(request, 'home.html', {'images':images})

def contact_us(request):

    p = None
    text = None

    try:
        p = Pages.objects.get(title='Contact')
        text = p.text
    except ObjectDoesNotExist:
        pass

    return render(request, 'pages/contact_us.html', {'text':text})

def about_us(request):

    p = None
    text = None

    try:
        p = Pages.objects.get(title='About')
        text = p.text
    except ObjectDoesNotExist:
        pass

    return render(request, 'pages/about_us.html', {'text':text})



# error views

def server_error(request):
    return render(request, 'errors/500.html')

def not_found(request):
    return render(request, 'errors/404.html')

def permission_denied(request):
    return render(request, 'errors/403.html')

def bad_request(request):
    return render(request, 'errors/400.html')

# Create your views here.
